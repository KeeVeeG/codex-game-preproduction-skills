"""Prepare immutable, whole-frame image attachments locally; never send a request."""
import argparse
import hashlib
from io import BytesIO
import json
from pathlib import Path

from PIL import Image, ImageCms, ImageOps


def digest(data):
    return hashlib.sha256(data).hexdigest()


def canonical(value):
    return (json.dumps(value, ensure_ascii=False, sort_keys=True, indent=2) + "\n").encode("utf-8")


def positive(value):
    number = int(value)
    if number < 1:
        raise argparse.ArgumentTypeError("must be positive")
    return number


def bounded(root, value):
    path = (root / value).resolve()
    if not path.is_relative_to(root):
        raise ValueError(f"Path outside root: {path}")
    return path


def check_destination(path, data, output, sources):
    resolved = path.resolve()
    if not resolved.is_relative_to(output) or resolved in sources or path.is_symlink():
        raise ValueError(f"Unsafe output destination: {path}")
    if path.exists() and (not path.is_file() or path.read_bytes() != data):
        raise ValueError(f"Existing output differs; refusing overwrite: {path}")


def write_immutable(path, data, output, sources):
    check_destination(path, data, output, sources)
    try:
        with path.open("xb") as stream:
            stream.write(data)
    except FileExistsError:
        check_destination(path, data, output, sources)
    if path.read_bytes() != data:
        raise ValueError(f"Written output verification failed: {path}")


def prepare(source, raw, root, output, settings, args):
    relative = source.relative_to(root).as_posix()
    source_hash = digest(raw)
    with Image.open(BytesIO(raw)) as original:
        if original.format not in {"JPEG", "PNG", "WEBP", "BMP", "TIFF", "GIF"}:
            raise ValueError(f"Unsupported raster format: {relative} ({original.format})")
        if getattr(original, "n_frames", 1) != 1 or getattr(original, "is_animated", False):
            raise ValueError(f"Animated or multi-frame image unsupported: {relative}")
        original.load()
        source_dimensions = list(original.size)
        oriented = ImageOps.exif_transpose(original)
        oriented_dimensions = list(oriented.size)
        rgba = oriented.convert("RGBA")
        transparent = rgba.getchannel("A").getextrema()[0] < 255
        preview = rgba if transparent else oriented.convert("RGB")
        output_icc = None
        color_method = "No embedded ICC; existing channel conversion"
        if "icc_profile" in original.info:
            try:
                source_profile = ImageCms.ImageCmsProfile(BytesIO(original.info["icc_profile"]))
                profile_bytes = bytearray(ImageCms.ImageCmsProfile(ImageCms.createProfile("sRGB")).tobytes())
                # Fix generated timestamp and leave profile ID unspecified for deterministic reuse.
                profile_bytes[24:36] = bytes.fromhex("07d000010001000000000000")
                profile_bytes[84:100] = bytes(16)
                output_icc = bytes(profile_bytes)
                destination_profile = ImageCms.ImageCmsProfile(BytesIO(output_icc))
                color_input = oriented
                if oriented.mode in {"RGBA", "RGBa", "RGBX", "P", "PA"}:
                    color_input = rgba.convert("RGB")
                elif oriented.mode in {"LA", "La"}:
                    color_input = oriented.convert("LA").getchannel("L")
                preview = ImageCms.profileToProfile(color_input, source_profile, destination_profile,
                                                   renderingIntent=ImageCms.Intent.RELATIVE_COLORIMETRIC, outputMode="RGB")
                if transparent:
                    preview.putalpha(rgba.getchannel("A"))
                color_method = "Embedded ICC converted to sRGB by LittleCMS; relative colorimetric; alpha retained"
            except (OSError, ValueError, TypeError, ImageCms.PyCMSError) as error:
                raise ValueError(f"Invalid or unsupported embedded ICC profile: {error}") from error
        preview.thumbnail((args.max_edge, args.max_edge), Image.Resampling.LANCZOS)
        image_format = "PNG" if transparent else "JPEG"
        encoded = BytesIO()
        options = {} if transparent else {"quality": args.quality, "subsampling": 0}
        # Strip source metadata, then explicitly attach the correct converted color profile.
        preview.info.clear()
        if output_icc is not None:
            options["icc_profile"] = output_icc
        preview.save(encoded, format=image_format, optimize=True, **options)
        data = encoded.getvalue()
        dimensions = list(preview.size)
    if len(data) > min(args.max_image_bytes, args.max_batch_bytes):
        raise ValueError(
            f"Preview exceeds image or single-image batch budget: {relative}: {len(data)} bytes "
            f"(image {args.max_image_bytes}, batch {args.max_batch_bytes}). "
            "Choose a smaller --max-edge, lower --quality for JPEG, or explicit larger budgets."
        )
    with Image.open(BytesIO(data)) as check:
        check.load()
        if list(check.size) != dimensions or check.format != image_format:
            raise ValueError(f"Encoded image verification failed: {relative}")
        if check.info.get("icc_profile") != output_icc:
            raise ValueError(f"Encoded color profile verification failed: {relative}")
    identity = digest(canonical({"path": relative, "sha256": source_hash, "settings": settings}))
    target = output / ("preview-" + identity + (".png" if transparent else ".jpg"))
    record = {
        "source": {"path": relative, "sha256": source_hash, "bytes": len(raw),
                   "dimensions": source_dimensions, "orientedDimensions": oriented_dimensions},
        "transport": {"path": target.relative_to(root).as_posix(), "sha256": digest(data),
                      "bytes": len(data), "dimensions": dimensions, "format": image_format},
        "method": {**settings, "alphaPreserved": transparent, "wholeFrame": True, "cropped": False,
                   "colorConversion": color_method, "outputICC": None if output_icc is None else
                   {"colorSpace": "sRGB", "sha256": digest(output_icc)}},
    }
    return target, data, record


def main():
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='Example (two explicit images):\n  python prepare-review-images.py '
               '"assets/first.png" "assets/second.png" --output-dir "docs/reviews/transport"\n'
               'Budgets are configurable starting values, not model/API limits. '
               'Batch bytes exclude base64 expansion and request overhead. No automatic quality search.',
    )
    parser.add_argument("sources", nargs="+", help="Explicit raster files, relative to root or absolute within root")
    parser.add_argument("--root", type=Path, default=Path.cwd(), help="Game project root (default: current working directory)")
    parser.add_argument("--output-dir", required=True, type=Path, help="Output directory inside root; existing different files are never overwritten")
    parser.add_argument("--max-edge", type=positive, default=1024, help="Maximum preview edge in pixels (default: 1024)")
    parser.add_argument("--quality", type=positive, default=82, help="JPEG quality 1–100 (default: 82); PNG keeps alpha")
    parser.add_argument("--max-image-bytes", type=positive, default=500000, help="Encoded bytes per image (default: 500000)")
    parser.add_argument("--max-batch-bytes", type=positive, default=580000, help="Total encoded bytes per batch (default: 580000)")
    parser.add_argument("--max-images", type=positive, default=8, help="Maximum image count per batch (default: 8)")
    args = parser.parse_args()
    try:
        root = args.root.resolve(strict=True)
        if not root.is_dir() or args.quality > 100:
            raise ValueError("Root must be a directory and JPEG quality must be 1–100")
        output = bounded(root, args.output_dir)
        if output.exists() and not output.is_dir():
            raise ValueError(f"Output directory is not a directory: {output}")
        sources = [bounded(root, value) for value in args.sources]
        if len(set(sources)) != len(sources):
            raise ValueError("Duplicate source paths are not allowed")
        for source in sources:
            if not source.is_file() or source.suffix.lower() in {".svg", ".svgz"}:
                raise ValueError(f"Expected an existing supported raster file, not SVG: {source}")
        settings = {"maxEdge": args.max_edge, "jpegQuality": args.quality, "jpegSubsampling": 0,
                    "resize": "LANCZOS thumbnail; preserve aspect; never upscale", "orientation": "EXIF transpose",
                    "opaqueFormat": "JPEG", "transparentFormat": "PNG", "metadata": "stripped except converted sRGB ICC",
                    "colorPolicy": "embedded ICC to sRGB, relative colorimetric; untagged input uses existing channel conversion"}
        prepared = []
        for source in sources:
            try:
                prepared.append(prepare(source, source.read_bytes(), root, output, settings, args))
            except (OSError, ValueError, Image.DecompressionBombError) as error:
                raise ValueError(f"Cannot prepare {source.relative_to(root)}: {error}") from error
        records = [item[2] for item in prepared]
        batches = []
        for row in records:
            transport = row["transport"]
            if not batches or batches[-1]["count"] >= args.max_images or batches[-1]["bytes"] + transport["bytes"] > args.max_batch_bytes:
                batches.append({"id": len(batches) + 1, "count": 0, "bytes": 0, "estimatedBase64Bytes": 0,
                                "files": [], "status": "prepared_local_only", "dispatchStatus": "not_sent"})
            batch = batches[-1]
            batch["count"] += 1
            batch["bytes"] += transport["bytes"]
            batch["estimatedBase64Bytes"] += 4 * ((transport["bytes"] + 2) // 3)
            batch["files"].append(transport["path"])
        if any(b["count"] > args.max_images or b["bytes"] > args.max_batch_bytes for b in batches):
            raise ValueError("Batch budget verification failed")
        manifest = {"schemaVersion": "1.0", "root": str(root), "status": "prepared_local_only",
                    "dispatchStatus": "not_sent", "images": records, "batches": batches,
                    "budgets": {"maxImageBytes": args.max_image_bytes, "maxBatchBytes": args.max_batch_bytes,
                                "maxImagesPerBatch": args.max_images, "modelLimitsClaimed": False},
                    "limitations": ["Downscaling and JPEG loss can hide small text and fine details; inspect originals for those checks.",
                                    "Batch bytes count encoded files; estimatedBase64Bytes excludes request envelopes and other content.",
                                    "Only explicit files are prepared. No network request or model review has occurred."]}
        manifest_data = canonical(manifest)
        manifest_path = output / ("manifest-" + digest(manifest_data) + ".json")
        for path, data, _ in prepared:
            check_destination(path, data, output, sources)
        check_destination(manifest_path, manifest_data, output, sources)
        for source, row in zip(sources, records):
            if digest(source.read_bytes()) != row["source"]["sha256"]:
                raise ValueError(f"Source changed during preparation: {source}")
        output.mkdir(parents=True, exist_ok=True)
        for path, data, _ in prepared:
            write_immutable(path, data, output, sources)
        for source, row in zip(sources, records):
            if digest(source.read_bytes()) != row["source"]["sha256"]:
                raise ValueError(f"Source changed before manifest publication: {source}")
        write_immutable(manifest_path, manifest_data, output, sources)
        print(json.dumps({"status": "prepared_local_only", "dispatchStatus": "not_sent",
                          "manifest": str(manifest_path), "imageCount": len(records), "batchCount": len(batches)}, ensure_ascii=False))
    except (OSError, ValueError, Image.DecompressionBombError) as error:
        parser.exit(2, f"Error: {error}\n")


if __name__ == "__main__":
    main()
