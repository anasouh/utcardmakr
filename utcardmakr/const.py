from enum import Enum
from os import path

package_fp = path.dirname(path.abspath(__file__))

CARD_BG = {
    "common": {
        "bronze": path.join(package_fp, "assets/cards/common/bronze.png"),
        "silver": path.join(package_fp, "assets/cards/common/silver.png"),
        "gold": path.join(package_fp, "assets/cards/common/gold.png"),
    },
    "rare": {
        "bronze": path.join(package_fp, "assets/cards/rare/bronze.png"),
        "silver": path.join(package_fp, "assets/cards/rare/silver.png"),
        "gold": path.join(package_fp, "assets/cards/rare/gold.png"),
    },
}

CARD_BG_SMALL = {
    "common": {
        "bronze": path.join(package_fp, "assets/cards/small/common/bronze.png"),
        "silver": path.join(package_fp, "assets/cards/small/common/silver.png"),
        "gold": path.join(package_fp, "assets/cards/small/common/gold.png"),
    },
    "rare": {
        "bronze": path.join(package_fp, "assets/cards/small/rare/bronze.png"),
        "silver": path.join(package_fp, "assets/cards/small/rare/silver.png"),
        "gold": path.join(package_fp, "assets/cards/small/rare/gold.png"),
    },
}

def get_font_fp(font_name: str):
    return path.join(package_fp, font_name)

class Rarity(Enum):
    COMMON = "common"
    RARE = "rare"

class Color(Enum):
    BRONZE = "bronze"
    SILVER = "silver"
    GOLD = "gold"