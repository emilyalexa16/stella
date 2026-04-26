GOLD = {
    "SaveGame": {
        "player": {
            "money": "1000"   # triggers first branch
        },
        "mine_lowestLevelReached": "200",
        "goldenWalnutsFound": "150",
        "locations": {
            "GameLocation": [
                {
                    "@xsi:type": "CommunityCenter",
                    "numberOfStarsOnPlaque": "5"
                }
            ]
        }
    }
}

MINE = {
    "SaveGame": {
        "player": {
            "money": "10000"
        },
        "mine_lowestLevelReached": "100",  # triggers second branch
        "goldenWalnutsFound": "150",
        "locations": {
            "GameLocation": [
                {
                    "@xsi:type": "CommunityCenter",
                    "numberOfStarsOnPlaque": "5"
                }
            ]
        }
    }
}

BUNDLES = {
    "SaveGame": {
        "player": {
            "money": "10000"
        },
        "mine_lowestLevelReached": "200",
        "goldenWalnutsFound": "150",
        "locations": {
            "GameLocation": [
                {
                    "@xsi:type": "CommunityCenter",
                    "numberOfStarsOnPlaque": "3"  # triggers third branch
                }
            ]
        }
    }
}

WALNUTS = {
    "SaveGame": {
        "player": {
            "money": "10000"
        },
        "mine_lowestLevelReached": "200",
        "goldenWalnutsFound": "50",  # triggers fourth branch
        "locations": {
            "GameLocation": [
                {
                    "@xsi:type": "CommunityCenter",
                    "numberOfStarsOnPlaque": "5"
                }
            ]
        }
    }
}

WELL_PROGRESSED = {
    "SaveGame": {
        "player": {
            "money": "10000"
        },
        "mine_lowestLevelReached": "200",
        "goldenWalnutsFound": "150",
        "locations": {
            "GameLocation": [
                {
                    "@xsi:type": "CommunityCenter",
                    "numberOfStarsOnPlaque": "5"
                }
            ]
        }
    }
}