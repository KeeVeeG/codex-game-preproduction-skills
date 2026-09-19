"""Exercise image attachment preparation in isolated temporary game projects.

Requires Pillow in the running Python environment. No network calls are made.
"""
import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

from PIL import Image


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


class ImageTransportTests(unittest.TestCase):
    script = None

    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory(prefix="game-image-transport-")
        self.addCleanup(self.temporary.cleanup)
        self.parent = Path(self.temporary.name).resolve()
        self.root = self.parent / "game"
        self.root.mkdir()
        rgb = Image.new("RGB", (1600, 800))
        rgb.paste((240, 20, 20), (0, 0, 800, 400))
        rgb.paste((20, 240, 20), (800, 0, 1600, 400))
        rgb.paste((20, 20, 240), (0, 400, 800, 800))
        rgb.paste((240, 220, 20), (800, 400, 1600, 800))
        # Distinct edge markers expose common centered-crop mistakes.
        rgb.paste((0, 220, 220), (0, 0, 100, 100))
        rgb.paste((220, 0, 220), (1500, 0, 1600, 100))
        rgb.paste((245, 245, 245), (0, 700, 100, 800))
        rgb.paste((10, 10, 10), (1500, 700, 1600, 800))
        rgb.save(self.root / "wide image.png")
        alpha = Image.new("RGBA", (400, 200), (40, 80, 120, 0))
        alpha.paste((200, 70, 30, 127), (100, 50, 300, 150))
        alpha.save(self.root / "alpha.png")
        Image.new("RGB", (40, 20), (60, 90, 120)).save(self.root / "small.png")
        self.sources = ["wide image.png", "alpha.png", "small.png"]
        self.original_hashes = {name: sha256(self.root / name) for name in self.sources}

    def invoke(self, *options, sources=None, output="transport", explicit_root=True):
        command = [sys.executable, "-X", "utf8", str(self.script)]
        command += list(self.sources if sources is None else sources)
        command += ["--output-dir", output, "--max-edge", "320", "--max-images", "2"]
        if explicit_root:
            command += ["--root", str(self.root)]
        command += list(options)
        return subprocess.run(command, cwd=self.root, text=True, encoding="utf-8", capture_output=True, check=False)

    def successful(self, **kwargs):
        result = self.invoke(**kwargs)
        self.assertEqual(result.returncode, 0, result.stderr)
        response = json.loads(result.stdout)
        self.assertEqual(response["status"], "prepared_local_only")
        self.assertEqual(response["dispatchStatus"], "not_sent")
        manifest_path = Path(response["manifest"])
        self.assertTrue(manifest_path.resolve().is_relative_to(self.root))
        self.assertTrue(manifest_path.is_file())
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        return response, manifest, manifest_path

    def assert_sources_unchanged(self):
        self.assertEqual(self.original_hashes, {name: sha256(self.root / name) for name in self.sources})

    def test_full_frame_dimensions_alpha_and_real_hashes(self):
        response, manifest, manifest_path = self.successful()
        self.assertEqual(response["imageCount"], 3)
        self.assertEqual(response["batchCount"], 2)
        self.assertEqual(manifest["status"], "prepared_local_only")
        self.assertEqual(manifest["dispatchStatus"], "not_sent")
        self.assertFalse(manifest["budgets"]["modelLimitsClaimed"])
        self.assertEqual(manifest_path.stem, "manifest-" + sha256(manifest_path))
        expected_dimensions = {"wide image.png": [320, 160], "alpha.png": [320, 160], "small.png": [40, 20]}
        records = {}
        for row in manifest["images"]:
            source, transport = row["source"], row["transport"]
            records[source["path"]] = row
            original = self.root / source["path"]
            target = self.root / transport["path"]
            self.assertTrue(target.resolve().is_relative_to(self.root))
            self.assertEqual(source["sha256"], sha256(original))
            self.assertEqual(source["bytes"], original.stat().st_size)
            self.assertEqual(transport["sha256"], sha256(target))
            self.assertEqual(transport["bytes"], target.stat().st_size)
            self.assertEqual(transport["dimensions"], expected_dimensions[source["path"]])
            self.assertLessEqual(transport["bytes"], manifest["budgets"]["maxImageBytes"])
            self.assertTrue(row["method"]["wholeFrame"])
            self.assertFalse(row["method"]["cropped"])
            with Image.open(target) as image:
                self.assertEqual(list(image.size), transport["dimensions"])
                self.assertEqual(image.format, transport["format"])
        with Image.open(self.root / records["wide image.png"]["transport"]["path"]) as image:
            # Check actual edge content, not only the self-reported wholeFrame flag.
            for position, expected in [((10, 10), (0, 220, 220)), ((309, 10), (220, 0, 220)),
                                       ((10, 149), (245, 245, 245)), ((309, 149), (10, 10, 10))]:
                actual = image.getpixel(position)
                self.assertTrue(all(abs(a - b) <= 8 for a, b in zip(actual, expected)), (position, actual))
        with Image.open(self.root / records["alpha.png"]["transport"]["path"]) as image:
            self.assertEqual(image.format, "PNG")
            self.assertEqual(image.mode, "RGBA")
            self.assertEqual(image.getpixel((2, 2))[3], 0)
            self.assertEqual(image.getpixel((160, 80))[3], 127)
        self.assert_sources_unchanged()

    def test_batches_match_actual_files_and_encoded_budgets(self):
        _, manifest, _ = self.successful()
        expected = [row["transport"]["path"] for row in manifest["images"]]
        actual = []
        for batch in manifest["batches"]:
            actual.extend(batch["files"])
            sizes = [(self.root / name).stat().st_size for name in batch["files"]]
            self.assertEqual(batch["count"], len(sizes))
            self.assertLessEqual(batch["count"], 2)
            self.assertEqual(batch["bytes"], sum(sizes))
            self.assertEqual(batch["estimatedBase64Bytes"], sum(4 * ((size + 2) // 3) for size in sizes))
            self.assertLessEqual(batch["bytes"], manifest["budgets"]["maxBatchBytes"])
            self.assertEqual(batch["dispatchStatus"], "not_sent")
        self.assertEqual(actual, expected)
        self.assert_sources_unchanged()

    def test_repeat_reuses_immutable_outputs(self):
        first, _, _ = self.successful()
        output = self.root / "transport"
        before = {path.name: (sha256(path), path.stat().st_mtime_ns) for path in output.iterdir()}
        second, _, _ = self.successful()
        after = {path.name: (sha256(path), path.stat().st_mtime_ns) for path in output.iterdir()}
        self.assertEqual(first, second)
        self.assertEqual(before, after)
        self.assert_sources_unchanged()

    def test_default_root_is_game_working_directory(self):
        _, manifest, _ = self.successful(explicit_root=False, sources=["small.png"])
        self.assertEqual(Path(manifest["root"]), self.root)
        self.assertEqual(manifest["images"][0]["transport"]["dimensions"], [40, 20])
        self.assert_sources_unchanged()

    def test_source_outside_root_is_rejected_before_output(self):
        outside = self.parent / "outside.png"
        Image.new("RGB", (20, 10), (255, 0, 0)).save(outside)
        before = sha256(outside)
        result = self.invoke(sources=[str(outside)], output="rejected")
        self.assertEqual(result.returncode, 2)
        self.assertIn("outside root", result.stderr.lower())
        self.assertFalse(result.stdout.strip())
        self.assertFalse((self.root / "rejected").exists())
        self.assertEqual(sha256(outside), before)
        self.assert_sources_unchanged()

    def test_output_outside_root_is_rejected(self):
        result = self.invoke(output="../outside-output")
        self.assertEqual(result.returncode, 2)
        self.assertFalse(result.stdout.strip())
        self.assertFalse((self.parent / "outside-output").exists())
        self.assert_sources_unchanged()

    def test_size_overflow_has_no_manifest_or_output_claim(self):
        result = self.invoke("--max-image-bytes", "1", output="too-large")
        self.assertEqual(result.returncode, 2)
        self.assertIn("budget", result.stderr.lower())
        self.assertFalse(result.stdout.strip())
        self.assertFalse((self.root / "too-large").exists())
        self.assert_sources_unchanged()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1], help="Skill repository root")
    args = parser.parse_args()
    ImageTransportTests.script = (args.root / ".agents" / "skills" / "00-game-preproduction" / "scripts" / "prepare-review-images.py").resolve()
    if not ImageTransportTests.script.is_file():
        parser.error("Image preparation script is missing from the selected repository")
    result = unittest.TextTestRunner(verbosity=2).run(unittest.defaultTestLoader.loadTestsFromTestCase(ImageTransportTests))
    return 0 if result.wasSuccessful() else 1


if __name__ == "__main__":
    sys.exit(main())
