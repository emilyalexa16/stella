import random
from collections import defaultdict

class FriendshipRLAgent:
    def __init__(self, epsilon=0.3, alpha=0.1, gamma=0.9):
        self.epsilon = epsilon # exploration rate
        self.alpha = alpha # learning rate
        self.gamma = gamma # discount factor
        self.q_table = defaultdict(lambda: {"gift": 0.0, "talk": 0.0, "skip": 0.0})

    def _state_key(self, name, friend_data):
        pts_bin = int(friend_data["Points"]) / 500 # sorts friendship points into 5 bins (e.g. 0-499, 500-999, etc.)
        gifts_today = min(int(friend_data["GiftsToday"]), 1) # returns 1 if gift has been given today
        gifts_week = min(int(friend_data["GiftsThisWeek"]), 2) # returns how many gifts have been given this week, anything over 2 is reduced to 2
        talked = int(friend_data["TalkedToToday"] == "true") # returns 1 if person has been talked to today
        status = friend_data["Status"] # how friendly the person is towards The Player
        return f"{name}|{pts_bin}|{gifts_today}|{gifts_week}|{talked}|{status}"

    def _valid_actions(self, friend_data):
        actions = ["skip"]
        if not friend_data["TalkedToToday"] == "true":
            actions.append("talk")
        if int(friend_data["GiftsToday"]) < 1 and int(friend_data["GiftsThisWeek"]) < 2:
            actions.append("gift")
        return actions

    def _reward(self, friend_data, action):
        f = dict(friend_data)
        POSITIVE_STATUSES = ("Friendly", "Dating", "Engaged", "Married")
        NEGATIVE_STATUSES   = ("Hostile", "Divorced")

        if int(f["Points"]) >= 2500:
            return -20, f
        if action == "gift":
            if int(f["GiftsToday"]) < 1 and int(f["GiftsThisWeek"]) < 2:
                gain = 30 if f["Status"] in POSITIVE_STATUSES else 20
                f["Points"] = min(2500, int(f["Points"]) + gain) # 2500 is the maximum for friendship points
                f["GiftsToday"] = int(f["GiftsToday"]) + 1
                f["GiftsThisWeek"] = int(f["GiftsThisWeek"]) + 1
                return gain, f
        elif action == "talk":
            if not f["TalkedToToday"] == "true":
                f["Points"] = min(2500, int(f["Points"]) + 20)
                f["TalkedToToday"] = "true"
                return 20, f
        return 0, f  # skip

    def choose_action(self, state_key, friend_data):
        valid = self._valid_actions(friend_data)
        if random.random() < self.epsilon:
            return random.choice(valid)
        q = self.q_table[state_key]
        return max(valid, key=lambda a: q[a])

    def update(self, state_key, action, reward, next_key):
        old_q = self.q_table[state_key][action]
        next_max = max(self.q_table[next_key].values())
        self.q_table[state_key][action] = (
            old_q + self.alpha * (reward + self.gamma * next_max - old_q)
        )

    def get_friendship_focus(self, data):
        items = data["SaveGame"]["player"]["friendshipData"]["item"]
        best_name, best_q = None, float("-inf")

        for item in items:
            name       = item["key"]["string"]
            friendship = item["value"]["Friendship"]
            state_key  = self._state_key(name, friendship)
            valid      = self._valid_actions(friendship)
            q          = self.q_table[state_key]
            best_valid_q = max(q[a] for a in valid)

            if best_valid_q > best_q:
                best_q, best_name = best_valid_q, name

        return best_name

    def train_step(self, data):
        items = data["SaveGame"]["player"]["friendshipData"]["item"]
        for item in items:
            name = item["key"]["string"]
            friendship = dict(item["value"]["Friendship"])

            state_key = self._state_key(name, friendship)
            action = self.choose_action(state_key, friendship)
            reward, new_f = self._reward(friendship, action)
            next_key = self._state_key(name, new_f)
            self.update(state_key, action, reward, next_key)

def get_advanced_friendship_focus(data):
    agent = FriendshipRLAgent(epsilon=0.3, alpha=0.1, gamma=0.9)
    for i in range(1000): # 1000 game days
        agent.train_step(data)
    priority = agent.get_friendship_focus(data)
    return priority