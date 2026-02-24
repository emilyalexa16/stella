import os
import xmltodict

print("\nWelcome to the Stella AI! Please choose what topic you would like suggestions for: \n")
print("1: Friendships")
print("2: Skills")
print("3: Progression\n")
selection = int(input("Enter here: "))

# change the xml into a python dictionary so we can navigate/access items more easily
# file_path = os.path.expanduser("/Users/emilygotiangco/School/cmps_490/Saves/Ivans_401983009/Ivans_401983009")
file_path = os.path.expanduser("/Users/emilygotiangco/.config/StardewValley/Saves/Stella_430626840/Stella_430626840")
with open(file_path) as f:
    data = xmltodict.parse(f.read())

if selection == 1: # friendships
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

    print(f"\nFocus on {prioritized_friend['name']} next!\n")

if (selection == 2): # skills
    skills = ["Farming", "Fishing", "Foraging", "Mining", "Combat"]
    skills_xp = data["SaveGame"]["player"]["experiencePoints"]["int"]

    # Pair each skill with its XP
    skill_xp_pairs = zip(skills, skills_xp)

    # Find the pair with the max XP
    max_skill, max_xp = max(skill_xp_pairs, key=lambda pair: pair[1])

    print(f"\nFocus on {max_skill} next!\n")

if (selection == 3): # progression
    total_gold_earned = int(data["SaveGame"]["player"]["money"])
    mine_lowest_level_reached = int(data["SaveGame"]["mine_lowestLevelReached"])
    for loc in data["SaveGame"]["locations"]["GameLocation"]:
        if loc.get("@xsi:type") == "CommunityCenter":
            community_center_stars = int(loc["numberOfStarsOnPlaque"])
            break
    num_golden_walnuts = int(data["SaveGame"]["goldenWalnutsFound"])

    if total_gold_earned < 2000:
        print("\nYou need to earn more gold!\n")
    elif mine_lowest_level_reached < 150:
        print("\nReach the bottom of the village mine!\n")
    elif community_center_stars < 5:
        print("\nComplete the community center bundles!\n")
    elif num_golden_walnuts < 120:
        print("\nFind all golden walnuts!\n")
        