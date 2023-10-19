from enum import Enum
import pkgutil

CARD_BG = {
    "common": {
        "bronze": pkgutil.get_data(__name__, "assets/cards/common/bronze.png"),
        "silver": pkgutil.get_data(__name__, "assets/cards/common/silver.png"),
        "gold": pkgutil.get_data(__name__, "assets/cards/common/gold.png"),
    },
    "rare": {
        "bronze": pkgutil.get_data(__name__, "assets/cards/rare/bronze.png"),
        "silver": pkgutil.get_data(__name__, "assets/cards/rare/silver.png"),
        "gold": pkgutil.get_data(__name__, "assets/cards/rare/gold.png"),
    },
}

CARD_BG_SMALL = {
    "common": {
        "bronze": pkgutil.get_data(__name__, "assets/cards/small/common/bronze.png"),
        "silver": pkgutil.get_data(__name__, "assets/cards/small/common/silver.png"),
        "gold": pkgutil.get_data(__name__, "assets/cards/small/common/gold.png"),
    },
    "rare": {
        "bronze": pkgutil.get_data(__name__, "assets/cards/small/rare/bronze.png"),
        "silver": pkgutil.get_data(__name__, "assets/cards/small/rare/silver.png"),
        "gold": pkgutil.get_data(__name__, "assets/cards/small/rare/gold.png"),
    },
}

class Rarity(Enum):
    COMMON = "common"
    RARE = "rare"

class Color(Enum):
    BRONZE = "bronze"
    SILVER = "silver"
    GOLD = "gold"