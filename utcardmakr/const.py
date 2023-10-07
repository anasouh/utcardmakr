from enum import Enum

CARD_BG = {
    "common": {
        "bronze": "assets/cards/common/bronze.png",
        "silver": "assets/cards/common/silver.png",
        "gold": "assets/cards/common/gold.png",
    },
    "rare": {
        "bronze": "assets/cards/rare/bronze.png",
        "silver": "assets/cards/rare/silver.png",
        "gold": "assets/cards/rare/gold.png",
    },
}

CARD_BG_SMALL = {
    "common": {
        "bronze": "assets/cards/small/common/bronze.png",
        "silver": "assets/cards/small/common/silver.png",
        "gold": "assets/cards/small/common/gold.png",
    },
    "rare": {
        "bronze": "assets/cards/small/rare/bronze.png",
        "silver": "assets/cards/small/rare/silver.png",
        "gold": "assets/cards/small/rare/gold.png",
    },
}

class Rarity(Enum):
    COMMON = "common"
    RARE = "rare"

class Color(Enum):
    BRONZE = "bronze"
    SILVER = "silver"
    GOLD = "gold"