import unittest
from src.services.skills_service import get_skill_focus
from tests.fixtures.skills_fixtures import SKILLS_BASIC, SKILLS_TIE, SKILLS_ZERO

class TestSkillsService(unittest.TestCase):

    def test_skills_basic(self):
        result = get_skill_focus(SKILLS_BASIC)
        self.assertEqual(result, "Combat")

    def test_skills_tie(self):
        result = get_skill_focus(SKILLS_TIE)
        self.assertEqual(result, "Fishing")

    def test_skills_zero(self):
        result = get_skill_focus(SKILLS_ZERO)
        self.assertEqual(result, "Farming")

if __name__ == "__main__":
    unittest.main()