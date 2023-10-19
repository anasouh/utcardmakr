from PIL import Image
from utcardmakr.const import *

class Card:
    
    @staticmethod
    def create_base_card(rarity: Rarity, color: Color) -> Image.Image:
        pass

    @classmethod
    def create(cls, rarity: Rarity, color: Color, face_fp: str, overall: str, position: str, name: str, club_fp: str, country_fp: str) -> Image.Image:
        pass
