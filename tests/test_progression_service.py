import unittest
from src.services.progression_service import get_progression_focus
from tests.fixtures.progression_fixtures import (
    GOLD, MINE, BUNDLES, WALNUTS, WELL_PROGRESSED
)

class TestProgression(unittest.TestCase):

    def test_low_gold(self):
        self.assertEqual(get_progression_focus(GOLD), "You need to earn more gold!")

    def test_low_mine(self):
        self.assertEqual(get_progression_focus(MINE), "Reach the bottom of the village mine!")

    def test_low_cc(self):
        self.assertEqual(get_progression_focus(BUNDLES), "Complete the community center bundles!")

    def test_low_walnuts(self):
        self.assertEqual(get_progression_focus(WALNUTS), "Find all golden walnuts!")

    def test_success(self):
        self.assertEqual(get_progression_focus(WELL_PROGRESSED),
                         "You are well progressed! Keep up the good work!")

if __name__ == "__main__":
    unittest.main()