"""Validate the portable skill package using Python's standard library.

This is a structural check with a deliberately limited flat YAML reader, not
the official Codex skill validator or a semantic review of the instructions.
"""
import argparse
import json
import os
from pathlib import Path, PurePosixPath
import re
import sys
from urllib.parse import unquote, urlsplit


EXPECTED_SKILLS = (
    "00-game-preproduction", "01-game-project-stage-detect", "02-game-map-systems",
    "03-game-scope-check", "04-game-review-all-gdds", "05-game-consistency-check",
    "06-game-design-system", "07-game-balance-check", "07a-game-narrative-design",
    "07b-game-level-design", "07c-game-level-review", "08-game-ux-design",
    "09-game-ux-review", "09a-game-accessibility-localization", "10-game-art-bible",
    "10a-game-environment-production", "10b-game-audio-design",
    "10c-game-visual-reference-pack", "11-game-asset-spec", "11a-game-content-coverage",
    "12-game-create-architecture", "13-game-architecture-decision",
    "14-game-architecture-review", "15-game-create-control-manifest",
    "15a-game-technical-risk-review", "16-game-propagate-design-change",
    "17-game-create-epics", "17a-game-production-readiness", "18-game-create-stories",
    "19-game-qa-plan", "20-game-story-readiness", "21-game-gate-check",
)
ORCHESTRATOR = EXPECTED_SKILLS[0]
TEXT_SUFFIXES = {".md", ".json", ".py", ".yaml", ".yml", ".toml", ".txt"}


def without_fences(text):
    """Skip fenced examples; inline code outside links is otherwise untouched."""
    output, fence = [], None
    for line in text.splitlines():
        marker = re.match(r"^\s{0,3}(`{3,}|~{3,})", line)
        if fence:
            if marker and marker[1][0] == fence[0] and len(marker[1]) >= len(fence):
                fence = None
            continue
        if marker:
            fence = marker[1]
        else:
            output.append(line)
    return "\n".join(output)


def files_under(root):
    for directory, subdirs, filenames in os.walk(root):
        subdirs[:] = [name for name in subdirs if name not in {".git", "__pycache__", ".venv", "node_modules"}]
        for name in filenames:
            yield Path(directory) / name


class Validation:
    def __init__(self, root):
        self.root = root.resolve()
        self.skills = self.root / ".agents" / "skills"
        self.entry = self.skills / ORCHESTRATOR
        self.errors = []
        self.counts = {"skills": 0, "stages": 0, "rechecks": 0, "markdown_files": 0, "local_links": 0}

    def require(self, condition, message):
        if not condition:
            self.errors.append(message)
        return bool(condition)

    def read_json(self, path):
        try:
            return json.loads(path.read_text(encoding="utf-8"))
        except (OSError, UnicodeError, ValueError) as error:
            self.errors.append(f"Cannot read JSON {path.relative_to(self.root)}: {error}")
            return {}

    def local_path(self, origin, target, boundary=None, must_exist=True):
        decoded = unquote(target)
        self.require(not re.match(r"^(?:[A-Za-z]:|[/\\]|~[/\\])", decoded),
                     f"Absolute/nonportable path in {origin.relative_to(self.root)}: {target}")
        normalized = decoded.replace("\\", "/")
        resolved = (origin.parent / normalized).resolve()
        allowed = (boundary or self.root).resolve()
        if not self.require(resolved.is_relative_to(allowed),
                            f"Path escapes allowed root in {origin.relative_to(self.root)}: {target}"):
            return
        if must_exist:
            self.require(resolved.exists(), f"Missing local target in {origin.relative_to(self.root)}: {target}")

    def check_skills(self):
        if not self.require(self.skills.is_dir(), "Missing .agents/skills directory"):
            return
        self.require(self.skills.resolve().is_relative_to(self.root), "Skills directory resolves outside repository")
        found = {path.parent.name for path in self.skills.glob("*/SKILL.md")}
        expected = set(EXPECTED_SKILLS)
        self.require(found == expected,
                     f"Skill inventory mismatch; missing={sorted(expected - found)}, extra={sorted(found - expected)}")
        self.counts["skills"] = len(found)
        for name in sorted(found):
            path = self.skills / name / "SKILL.md"
            if not self.require(path.resolve().is_relative_to(self.skills.resolve()), f"Skill resolves outside portable package: {name}"):
                continue
            content = path.read_text(encoding="utf-8")
            match = re.match(r"\A---\n(.*?)\n---(?:\n|$)", content, re.DOTALL)
            if not self.require(match is not None, f"{name}: missing YAML frontmatter"):
                continue
            fields = {}
            for line in match[1].splitlines():
                if not line.strip() or line.lstrip().startswith("#"):
                    continue
                pair = re.fullmatch(r"([a-z][a-z0-9_-]*):[ \t]*(.*)", line)
                if not self.require(pair is not None, f"{name}: unsupported non-flat YAML line"):
                    continue
                key, value = pair.groups()
                self.require(key not in fields, f"{name}: duplicate frontmatter key {key}")
                if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
                    value = value[1:-1]
                self.require(value not in {"|", ">", "|-", ">-"}, f"{name}: multiline YAML unsupported by this validator")
                fields[key] = value
            self.require(fields.get("name") == name, f"{name}: frontmatter name differs from directory")
            self.require(re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name) is not None and len(name) < 64,
                         f"{name}: invalid skill name")
            self.require(bool(fields.get("description", "").strip()) and len(fields.get("description", "")) <= 1024,
                         f"{name}: description missing or exceeds 1024 characters")
            self.require(bool(content[match.end():].strip()), f"{name}: empty instructions")

    def check_workflow(self):
        path = self.entry / "references" / "workflow.json"
        workflow = self.read_json(path)
        if not self.require(isinstance(workflow, dict), "workflow must be an object"):
            return
        self.require(workflow.get("orchestrator") == ORCHESTRATOR, "workflow orchestrator mismatch")
        self.require(workflow.get("resource_path_base") == "orchestrator_directory",
                     "workflow must explicitly resolve resource paths from the orchestrator directory")
        stages = workflow.get("stages", [])
        if not self.require(isinstance(stages, list) and all(isinstance(row, dict) for row in stages),
                            "workflow stages must be a list of objects"):
            return
        names = [row.get("skill") for row in stages]
        ids = [row.get("id") for row in stages]
        expected = set(EXPECTED_SKILLS[1:])
        self.require(all(isinstance(name, str) for name in names), "stage skill names must be strings")
        valid_names = [name for name in names if isinstance(name, str)]
        self.require(set(valid_names) == expected and len(valid_names) == len(expected),
                     "workflow must contain each of the 31 stage skills exactly once")
        self.require(workflow.get("stage_count") == len(stages) == 31, "workflow stage_count must equal 31 stages")
        valid_ids = [item for item in ids if isinstance(item, str)]
        self.require(len(valid_ids) == len(stages) and len(set(valid_ids)) == len(valid_ids), "stage ids must be unique strings")
        graph = {}
        for row in stages:
            name, after = row.get("skill"), row.get("after")
            if not isinstance(name, str):
                continue
            self.require(row.get("id") == name.split("-", 1)[0], f"stage id does not match skill: {name}")
            self.require(row.get("mode") in {"primary", "on_change"}, f"invalid stage mode: {name}")
            if not self.require(isinstance(after, list) and all(isinstance(dep, str) for dep in after),
                                f"after must contain skill names: {name}"):
                continue
            self.require(len(after) == len(set(after)), f"duplicate dependency: {name}")
            self.require(all(dep in expected and dep != name for dep in after), f"invalid dependency: {name}")
            graph[name] = after
        visiting, visited = set(), set()

        def visit(name):
            if name in visiting:
                self.errors.append(f"Dependency cycle reaches {name}")
                return
            if name in visited:
                return
            visiting.add(name)
            for dep in graph.get(name, []):
                visit(dep)
            visiting.remove(name)
            visited.add(name)

        for name in graph:
            visit(name)
        self.counts["stages"] = len(stages)
        rechecks = workflow.get("rechecks", [])
        if self.require(isinstance(rechecks, list) and bool(rechecks), "rechecks must be a nonempty list"):
            for number, row in enumerate(rechecks, 1):
                if not self.require(isinstance(row, dict), f"recheck {number} must be an object"):
                    continue
                self.require(isinstance(row.get("trigger"), str) and bool(row["trigger"].strip()), f"recheck {number} has no trigger")
                for field in ("skills", "required_before"):
                    values = row.get(field)
                    self.require(isinstance(values, list) and bool(values)
                                 and all(isinstance(value, str) and value in expected for value in values),
                                 f"recheck {number}: invalid {field} references")
            self.counts["rechecks"] = len(rechecks)
        completion = workflow.get("completion", {})
        if self.require(isinstance(completion, dict), "completion must be an object"):
            self.require(completion.get("gate") == "21-game-gate-check", "completion must terminate at stage 21")
            gate_ancestors = set()

            def ancestors(name):
                for dep in graph.get(name, []):
                    if dep not in gate_ancestors:
                        gate_ancestors.add(dep)
                        ancestors(dep)

            ancestors("21-game-gate-check")
            primary = {row.get("skill") for row in stages if row.get("mode") == "primary"} - {"21-game-gate-check"}
            self.require(primary <= gate_ancestors, f"Primary stages do not reach final gate: {sorted(primary - gate_ancestors)}")
        reviews = workflow.get("subagent_reviews", {})
        if self.require(isinstance(reviews, dict), "subagent_reviews must be an object"):
            self.require(reviews.get("reviewer") == "codex_subagent", "workflow reviewer must be a Codex subagent")
            self.require(reviews.get("reviewer_source") == "profile.review.reviewer", "workflow must use profile.review.reviewer")
            self.require(reviews.get("requires_fresh_context") is True, "independent reviews require fresh context")
            checkpoints = reviews.get("checkpoints", [])
            if self.require(isinstance(checkpoints, list), "subagent review checkpoints must be a list"):
                expected_checkpoints = {"MR-DESIGN": "11a-game-content-coverage",
                                        "MR-TECH": "15a-game-technical-risk-review",
                                        "MR-HANDOFF": "20-game-story-readiness"}
                self.require(len(checkpoints) == 3 and {row.get("id"): row.get("after") for row in checkpoints if isinstance(row, dict)} == expected_checkpoints,
                             "workflow must retain all three review checkpoints and their timing")
                for row in checkpoints:
                    if not self.require(isinstance(row, dict), "subagent checkpoint must be an object"):
                        continue
                    self.require(row.get("after") in expected and row.get("before", "21-game-gate-check") in expected,
                                 f"invalid subagent checkpoint reference: {row.get('id')}")
            image_reviews = reviews.get("image_reviews", {})
            if isinstance(image_reviews, dict):
                self.require(image_reviews.get("stage") in expected, "invalid image review stage")
                self.require(image_reviews.get("requires_actual_visual_input") is True, "image reviews must require actual visual input")
            if isinstance(completion, dict):
                self.require(completion.get("requires_current_subagent_reviews") == "profile.review.required"
                             and completion.get("requires_per_image_subagent_reviews") == "profile.review.image_review_required",
                             "completion must preserve profile review requirements")
        # These paths are documented as relative to the orchestrator, not JSON's directory.
        workflow_paths = [workflow.get("profile"), completion.get("coverage") if isinstance(completion, dict) else None,
                          reviews.get("protocol") if isinstance(reviews, dict) else None]
        if isinstance(reviews, dict) and isinstance(reviews.get("image_reviews"), dict):
            workflow_paths.append(reviews["image_reviews"].get("transport_script"))
        for target in workflow_paths:
            if self.require(isinstance(target, str) and bool(target), "missing workflow resource path"):
                self.local_path(self.entry / "SKILL.md", target, self.skills)

    def check_profile(self):
        path = self.entry / "references" / "profile.template.json"
        profile = self.read_json(path)
        if not self.require(isinstance(profile, dict), "profile template must be an object"):
            return
        sources = profile.get("sources")
        if self.require(isinstance(sources, dict) and bool(sources), "profile.sources must be a nonempty semantic map"):
            for key, values in sources.items():
                valid = isinstance(key, str) and bool(key) and isinstance(values, list) and all(isinstance(v, str) and bool(v) for v in values)
                if not self.require(valid, f"profile.sources.{key} must be a list of explicit relative paths"):
                    continue
                for value in values:
                    self.profile_path(value, f"profile.sources.{key}")
        features, evidence = profile.get("features"), profile.get("feature_evidence")
        if self.require(isinstance(features, dict) and isinstance(evidence, dict), "features and feature_evidence must be objects"):
            for key, value in features.items():
                self.require(value in {"present", "absent", "unknown"}, f"invalid applicability: {key}")
                if value == "absent":
                    item = evidence.get(key, {})
                    self.require(isinstance(item, dict) and all(isinstance(item.get(k), str) and item[k].strip()
                                 for k in ("source", "reason", "reopen_when")), f"absent feature {key} lacks complete evidence")
        paths = profile.get("paths", {})
        if self.require(isinstance(paths, dict), "profile.paths must be an object"):
            for key in ("state_dir", "reference_dir"):
                self.profile_path(paths.get(key), f"profile.paths.{key}")
        review = profile.get("review", {})
        if self.require(isinstance(review, dict), "review must be an object"):
            self.require(review.get("reviewer") == "codex_subagent", "package default reviewer must be a Codex subagent")
            self.require(review.get("required") is True and review.get("image_review_required") is True,
                         "package default review requirements must remain explicit and enabled")
            self.require(not {"model", "adapter"} & review.keys(), "portable review policy must not configure an external model or adapter")
            self.require(bool(review.get("policy_source")), "review policy must record its source")

    def profile_path(self, value, label):
        if not self.require(isinstance(value, str) and bool(value), f"{label}: path must be a nonempty string"):
            return
        normalized = value.replace("\\", "/")
        self.require(not re.match(r"^(?:[A-Za-z]:|/|~[/\\])", normalized)
                     and ".." not in PurePosixPath(normalized).parts
                     and not any(char in value for char in "*?[]")
                     and not urlsplit(normalized).scheme,
                     f"{label}: expected explicit path inside game root: {value}")

    def check_documents(self):
        for path in files_under(self.root):
            if path.suffix not in TEXT_SUFFIXES:
                continue
            text = path.read_text(encoding="utf-8")
            self.require(re.search(r"[\u0400-\u04ff]", text) is None,
                         f"Untranslated Cyrillic text in English package: {path.relative_to(self.root)}")
            packaged = path.is_relative_to(self.skills)
            if packaged:
                self.require(path.resolve().is_relative_to(self.skills.resolve()), f"Packaged file escapes via symlink: {path.name}")
                # Scan executable instructions/resources, not external provenance records.
                patterns = (r"(?i)[A-Z]:[/\\](?:Users|Documents and Settings)[/\\]",
                            r"/(?:Users|home)/[^\s/<>]+/")
                for pattern in patterns:
                    self.require(re.search(pattern, text) is None,
                                 f"Project-specific or personal path in packaged file: {path.relative_to(self.root)}")
            if path.suffix != ".md":
                continue
            self.counts["markdown_files"] += 1
            clean = without_fences(text)
            targets = re.findall(r"!?\[[^\]\n]*\]\(\s*(<[^>\n]+>|[^\s)]+)(?:\s+[^)]*)?\)", clean)
            targets += re.findall(r"^\s{0,3}\[[^\]\n]+\]:\s*(<[^>\n]+>|\S+)", clean, re.MULTILINE)
            for target in targets:
                target = target.removeprefix("<").removesuffix(">")
                parsed = urlsplit(target)
                if parsed.scheme and not re.match(r"^[A-Za-z]:[/\\]", target):
                    continue
                if not parsed.path or target.startswith("//"):
                    continue
                self.counts["local_links"] += 1
                self.local_path(path, parsed.path, self.skills if packaged else self.root)

    def run(self):
        for check in (self.check_skills, self.check_workflow, self.check_profile, self.check_documents):
            try:
                check()
            except (OSError, UnicodeError, TypeError, ValueError, KeyError) as error:
                self.errors.append(f"{check.__name__} could not complete: {error}")
        return {"status": "PASS" if not self.errors else "FAIL", **self.counts, "errors": self.errors,
                "limitations": ["Flat YAML name/description validation only; run the official skill validator separately.",
                                "Markdown checks cover inline links and reference definitions outside fenced code; anchors, remote URLs and full CommonMark syntax are not verified.",
                                "Profile source bindings are type/path-checked; game files need not exist in the package template.",
                                "Structural checks and portability patterns do not prove design quality, complete genericity, or absence of every possible secret."]}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1], help="Repository root")
    args = parser.parse_args()
    result = Validation(args.root).run()
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["status"] == "PASS" else 1


if __name__ == "__main__":
    sys.exit(main())
