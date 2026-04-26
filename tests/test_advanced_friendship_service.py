import unittest
from unittest.mock import patch
from tests.fixtures.advanced_friendship_fixtures import FRIENDSHIP_DATA, SAVE_DATA

from src.services.advanced_friendship_service import (
    FriendshipRLAgent,
    get_advanced_friendship_focus
)

class TestAdvancedFriendshipService(unittest.TestCase):

    # state key
    def test_state_key(self):
        agent = FriendshipRLAgent(epsilon=0)

        key = agent._state_key("Alex", FRIENDSHIP_DATA)

        self.assertIn("Alex", key)
        self.assertIn("2.0", key)  # 1000 / 500

    # valid actions
    def test_valid_actions(self):
        agent = FriendshipRLAgent()

        actions = agent._valid_actions(FRIENDSHIP_DATA)

        self.assertIn("gift", actions)
        self.assertIn("talk", actions)
        self.assertIn("skip", actions)

    # reward for talking
    def test_reward_talk_action(self):
        agent = FriendshipRLAgent()

        reward, new_state = agent._reward(FRIENDSHIP_DATA, "talk")

        self.assertEqual(reward, 20)
        self.assertEqual(new_state["TalkedToToday"], "true")

    # choose action
    def test_choose_action_deterministic(self):
        agent = FriendshipRLAgent(epsilon=0)  # no exploration

        state_key = agent._state_key("Alex", FRIENDSHIP_DATA)

        action = agent.choose_action(state_key, FRIENDSHIP_DATA)

        self.assertIn(action, ["gift", "talk", "skip"])

    # train
    @patch("random.random", return_value=1)  # forces exploitation path
    @patch("random.choice", return_value="skip")
    def test_train_step_runs(self, mock_choice, mock_random):
        agent = FriendshipRLAgent(epsilon=0.3)

        agent.train_step(SAVE_DATA)

        self.assertTrue(len(agent.q_table) > 0)

    # full test
    def test_advanced_friendship_focus_runs(self):

        result = get_advanced_friendship_focus(SAVE_DATA)

        self.assertIsNotNone(result)
        self.assertEqual(result, "Alex")

if __name__ == "__main__":
    unittest.main()