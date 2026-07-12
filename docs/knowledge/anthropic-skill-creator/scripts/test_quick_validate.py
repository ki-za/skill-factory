import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from quick_validate import validate_skill


class ValidateSkillTests(unittest.TestCase):
    def test_accepts_claude_code_invocation_controls(self):
        with tempfile.TemporaryDirectory() as directory:
            skill = Path(directory)
            (skill / "SKILL.md").write_text(
                "---\n"
                "name: example\n"
                "description: Example skill\n"
                "disable-model-invocation: true\n"
                "user-invocable: true\n"
                "---\n"
                "Instructions.\n"
            )

            valid, message = validate_skill(skill)

        self.assertTrue(valid, message)


if __name__ == "__main__":
    unittest.main()
