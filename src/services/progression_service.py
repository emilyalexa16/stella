def get_progression_focus(data):
    total_gold_earned = int(data["SaveGame"]["player"]["money"])
    mine_lowest_level_reached = int(data["SaveGame"]["mine_lowestLevelReached"])
    for loc in data["SaveGame"]["locations"]["GameLocation"]:
        if loc.get("@xsi:type") == "CommunityCenter":
            community_center_stars = int(loc["numberOfStarsOnPlaque"])
            break
    num_golden_walnuts = int(data["SaveGame"]["goldenWalnutsFound"])

    if total_gold_earned < 2000:
        return "You need to earn more gold!"
    elif mine_lowest_level_reached < 150:
        return "Reach the bottom of the village mine!"
    elif community_center_stars < 5:
        return "Complete the community center bundles!"
    elif num_golden_walnuts < 120:
        return "Find all golden walnuts!"
    else:
        return "You are well progressed! Keep up the good work!"