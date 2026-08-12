from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "ba-zero-to-office-tutor" / "SKILL.md"
REF = ROOT / "skills" / "ba-zero-to-office-tutor" / "references"

class RepositoryContract(unittest.TestCase):
    def test_skill_exists_with_valid_frontmatter(self):
        text = SKILL.read_text(encoding="utf-8")
        self.assertTrue(text.startswith("---\n"))
        self.assertRegex(text, r"(?m)^name: ba-zero-to-office-tutor$")
        self.assertRegex(text, r"(?m)^description: Use when .+")

    def test_skill_contains_behavioral_contract(self):
        text = SKILL.read_text(encoding="utf-8").lower()
        for phrase in [
            "understanding over memorization",
            "do not diagnose",
            "urgent",
            "teach-back",
            "transfer",
            "one active learning objective",
        ]:
            self.assertIn(phrase, text)

    def test_required_references_exist(self):
        expected = [
            "curriculum.md",
            "teaching-protocol.md",
            "cognitive-load.md",
            "assessment-rubric.md",
            "learner-state.md",
            "office-case-bank.md",
            "technical-mental-maps.md",
        ]
        for name in expected:
            self.assertTrue((REF / name).exists(), name)

    def test_curriculum_covers_all_office_targets(self):
        text = (REF / "curriculum.md").read_text(encoding="utf-8").lower()
        targets = [
            "sdlc", "bpmn", "requirements", "programming", "backend",
            "frontend", "database", "api", "git", "devops", "system design"
        ]
        for target in targets:
            self.assertIn(target, text)

    def test_assessment_rejects_definition_only_mastery(self):
        text = (REF / "assessment-rubric.md").read_text(encoding="utf-8").lower()
        self.assertIn("definition", text)
        self.assertIn("not mastery", text)
        self.assertIn("0–5", text)

    def test_chatgpt_source_package_is_present(self):
        expected = [
            "chatgpt/GPT-INSTRUCTIONS.md",
            "chatgpt/BUILDER-PROMPT.md",
            "scripts/build.py",
            "INSTALL.md",
        ]
        for rel in expected:
            self.assertTrue((ROOT / rel).exists(), rel)
        self.assertEqual(len(list(REF.glob("*.md"))), 7)

    def test_no_false_chatgpt_self_install_claim(self):
        install = (ROOT / "INSTALL.md").read_text(encoding="utf-8").lower()
        prohibition_present = any(marker in install for marker in ["does not", "does **not**", "cannot"])
        self.assertTrue(prohibition_present)
        self.assertIn("github", install)
        self.assertIn("custom gpt", install)

    def test_readme_has_ai_onboarding_marker(self):
        text = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("AI / LLM INSTALLATION INSTRUCTIONS", text)

    def test_no_tbd_or_todo_in_public_docs(self):
        for path in list(ROOT.glob("*.md")) + list(REF.glob("*.md")) + list((ROOT / "chatgpt").glob("*.md")):
            text = path.read_text(encoding="utf-8")
            self.assertNotRegex(text, r"\b(TBD|TODO)\b", str(path))

if __name__ == "__main__":
    unittest.main()
