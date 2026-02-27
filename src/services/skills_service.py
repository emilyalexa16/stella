def get_skill_focus(data):# skills
    skills = ["Farming", "Fishing", "Foraging", "Mining", "Combat"]
    skills_xp = data["SaveGame"]["player"]["experiencePoints"]["int"]

    # Pair each skill with its XP
    skill_xp_pairs = zip(skills, skills_xp)

    # Find the pair with the max XP
    max_skill, max_xp = max(skill_xp_pairs, key=lambda pair: pair[1])

    return max_skill