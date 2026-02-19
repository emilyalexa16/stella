import os
import xmltodict

print("\nWelcome to the Stella AI! Please choose what topic you would like suggestions for: \n")
print("1: Friendships")
print("2: Skills")
print("3: Progression\n")
selection = input("Enter here: ")

# change the xml into a python dictionary so we can navigate/access items more easily
# file_path = os.path.expanduser("~/Downloads/Saves/Ivans_401983009/Ivans_401983009")
file_path = os.path.expanduser("/Users/emilygotiangco/.config/StardewValley/Saves/Stella_430626840/Stella_430626840")
with open(file_path) as f:
    data = xmltodict.parse(f.read())

# main tags
items = data["SaveGame"]["player"]["friendshipData"]["item"]

friends = []

for item in items:
    # more tags
    name = item["key"]["string"]
    friendship = item["value"]["Friendship"]

    # store what's in the innermost tags
    points = int(friendship["Points"])
    gifts_today = int(friendship["GiftsToday"])
    gifts_week = int(friendship["GiftsThisWeek"])
    talked_today = friendship["TalkedToToday"] == "true"
    status = str(friendship["Status"])

    # dynamic scoring formula
    score = points
    if gifts_today == 0:
        score += 100
    if gifts_week < 3:
        score += 50
    if talked_today:
        score -= 1000
    if status == "Friendly":
        score += 30
    if status == "Hostile":
        score -= 50

    friends.append({"name": name, "score": score})

prioritized_friend = max(friends, key=lambda f: f["score"])

print(f"\nFocus on {prioritized_friend['name']} next!")