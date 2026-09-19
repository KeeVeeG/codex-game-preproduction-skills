"""Regression tests for the package validator using isolated portable copies.

Only the Python standard library is required. Tests never modify the source
package and invoke its validator against copies containing only .agents/skills.
"""
import argparse
import copy
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest


class PackageValidatorTests(unittest.TestCase):
    repository = None

    def setUp(self):
        temporary = tempfile.TemporaryDirectory(prefix="game-package-validation-")
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name) / "portable package"
        self.skills = self.root / ".agents" / "skills"
        shutil.copytree(self.repository / ".agents" / "skills", self.skills)
        self.references = self.skills / "00-game-preproduction" / "references"

    def read_json(self, name):
        return json.loads((self.references / name).read_text(encoding="utf-8"))

    def write_json(self, name, value):
        (self.references / name).write_text(
            json.dumps(value, ensure_ascii=True, indent=2) + "\n", encoding="utf-8"
        )

    def validate(self):
        process = subprocess.run(
            [sys.executable, "-X", "utf8", str(self.repository / "tools" / "validate-package.py"),
             "--root", str(self.root)],
            cwd=self.root,
            text=True,
            encoding="utf-8",
            capture_output=True,
            check=False,
        )
        self.assertFalse(process.stderr, process.stderr)
        try:
            report = json.loads(process.stdout)
        except ValueError:
            self.fail(f"Validator did not return JSON: {process.stdout!r}")
        return process.returncode, report

    def assert_rejected(self, diagnostic):
        returncode, report = self.validate()
        self.assertEqual(returncode, 1, report)
        self.assertEqual(report["status"], "FAIL", report)
        self.assertTrue(any(diagnostic in error for error in report["errors"]), report)

    def test_skills_copy_passes_without_repository_docs_or_tools(self):
        self.assertEqual({path.name for path in self.root.iterdir()}, {".agents"})
        self.assertFalse((self.root / "docs").exists())
        self.assertFalse((self.root / "tools").exists())
        returncode, report = self.validate()
        self.assertEqual(returncode, 0, report)
        self.assertEqual(report["status"], "PASS", report)
        self.assertEqual(report["errors"], [])
        self.assertEqual(report["skills"], 32)
        self.assertEqual(report["stages"], 31)
        self.assertGreater(report["local_links"], 0)

    def test_each_required_review_checkpoint_cannot_be_removed(self):
        original = self.read_json("workflow.json")
        for checkpoint in ("MR-DESIGN", "MR-TECH", "MR-HANDOFF"):
            with self.subTest(checkpoint=checkpoint):
                changed = copy.deepcopy(original)
                rows = changed["subagent_reviews"]["checkpoints"]
                changed["subagent_reviews"]["checkpoints"] = [
                    row for row in rows if row["id"] != checkpoint
                ]
                self.write_json("workflow.json", changed)
                self.assert_rejected("retain all three review checkpoints")

    def test_actual_visual_input_cannot_be_disabled_or_omitted(self):
        original = self.read_json("workflow.json")
        for omit in (False, True):
            with self.subTest(omitted=omit):
                changed = copy.deepcopy(original)
                image_reviews = changed["subagent_reviews"]["image_reviews"]
                if omit:
                    del image_reviews["requires_actual_visual_input"]
                else:
                    image_reviews["requires_actual_visual_input"] = False
                self.write_json("workflow.json", changed)
                self.assert_rejected("image reviews must require actual visual input")

    def test_invalid_profile_review_configuration_is_rejected(self):
        original = self.read_json("profile.template.json")
        cases = (
            ("required", False, "review requirements must remain explicit and enabled"),
            ("image_review_required", False, "review requirements must remain explicit and enabled"),
            ("reviewer", "self_review", "reviewer must be a Codex subagent"),
            ("model", "unconfigured", "must not configure an external model or adapter"),
            ("adapter", "unconfigured", "must not configure an external model or adapter"),
            ("policy_source", "", "review policy must record its source"),
        )
        for key, value, diagnostic in cases:
            with self.subTest(field=key):
                changed = copy.deepcopy(original)
                changed["review"][key] = value
                self.write_json("profile.template.json", changed)
                self.assert_rejected(diagnostic)

    def test_review_configuration_must_be_an_object(self):
        profile = self.read_json("profile.template.json")
        profile["review"] = []
        self.write_json("profile.template.json", profile)
        self.assert_rejected("review must be an object")

    def test_completion_must_fail_cleanly_when_not_an_object(self):
        original = self.read_json("workflow.json")
        for value in ([], None, "invalid"):
            with self.subTest(completion=value):
                workflow = copy.deepcopy(original)
                workflow["completion"] = value
                self.write_json("workflow.json", workflow)
                self.assert_rejected("completion must be an object")

    def test_independent_review_requires_fresh_context(self):
        workflow = self.read_json("workflow.json")
        workflow["subagent_reviews"]["requires_fresh_context"] = False
        self.write_json("workflow.json", workflow)
        self.assert_rejected("independent reviews require fresh context")

    def test_broken_package_link_is_rejected(self):
        skill = self.skills / "01-game-project-stage-detect" / "SKILL.md"
        with skill.open("a", encoding="utf-8") as stream:
            stream.write("\n[Missing reference](missing-reference.md)\n")
        self.assert_rejected("Missing local target")

    def test_link_cannot_depend_on_repository_docs(self):
        outside = self.root / "docs" / "outside.md"
        outside.parent.mkdir()
        outside.write_text("# Outside the portable package\n", encoding="utf-8")
        skill = self.skills / "01-game-project-stage-detect" / "SKILL.md"
        with skill.open("a", encoding="utf-8") as stream:
            stream.write("\n[Outside reference](../../../docs/outside.md)\n")
        self.assert_rejected("Path escapes allowed root")

    def test_stage_dependency_cycle_is_rejected(self):
        workflow = self.read_json("workflow.json")
        stages = {row["id"]: row for row in workflow["stages"]}
        self.assertIn(stages["01"]["skill"], stages["02"]["after"])
        stages["01"]["after"].append(stages["02"]["skill"])
        self.write_json("workflow.json", workflow)
        self.assert_rejected("Dependency cycle reaches")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1],
                        help="Skill repository root")
    args = parser.parse_args()
    PackageValidatorTests.repository = args.root.resolve()
    if not (PackageValidatorTests.repository / "tools" / "validate-package.py").is_file():
        parser.error("Package validator is missing from the selected repository")
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(PackageValidatorTests)
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    return 0 if result.wasSuccessful() else 1


if __name__ == "__main__":
    sys.exit(main())
