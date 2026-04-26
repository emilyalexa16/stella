import unittest
from src.services.friendship_service import get_friendship_focus
from tests.fixtures.friendship_fixtures import FRIENDSHIP_POINTS

class TestFriendshipService(unittest.TestCase):

    def test_friendship_points(self):
        result = get_friendship_focus(FRIENDSHIP_POINTS)
        self.assertEqual(result, "Sebastian")