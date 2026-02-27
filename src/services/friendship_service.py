def get_friendship_focus(data):
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

        return prioritized_friend["name"]