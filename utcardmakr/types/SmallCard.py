from PIL import Image, ImageDraw, ImageFont
from utcardmakr.const import *
from utcardmakr.types import Card
from utcardmakr.utils import *

class SmallCard(Card):

    @staticmethod
    def create_base_card(rarity: Rarity, color: Color):
        img = Image.new("RGBA", (726, 897), (0, 0, 0, 0))
        card_bg = Image.open(CARD_BG_SMALL[rarity.value][color.value])
        card_bg = card_bg.resize((726, 897))
        img.paste(card_bg, (0, 0))
        return img

    @staticmethod
    def add_face(img: Image.Image, face_fp: str):
        face = Image.open(face_fp)
        pos = (184, 139)
        MAX_WIDTH = 482
        height = 529
        new_width = int((height / face.size[1]) * face.size[0])
        if new_width > MAX_WIDTH:
            diff = new_width - MAX_WIDTH
            height -= diff
            new_width = MAX_WIDTH
            pos = (pos[0], pos[1]+diff)
        face = face.resize((new_width, height))
        try:
            img.paste(face, pos, mask=face)
        except ValueError:
            img.paste(face, pos)

    @staticmethod
    def add_overall(img: Image.Image, overall: str):
        draw = ImageDraw.Draw(img)
        draw.text(
            (44.91, 122.76),
            overall,
            fill="#40351d",
            font=ImageFont.truetype(
                "assets/fonts/condensed/Numbers-Bold.ttf", size=124
            ),
            align="center",
        )

    @staticmethod
    def add_position(img: Image.Image, position: str):
        draw = ImageDraw.Draw(img)
        TEXTBOX_W = 120
        TEXTBOX_X = 50
        font = ImageFont.truetype(
            "assets/fonts/condensed/CruyffSansCondensed+DINArabic+SSTThai-Regular.otf", size=56
        )
        _, _, w, h = draw.textbbox(
            (0, 0),
            position,
            font=font,
            align="center",
        )
        draw.text((((TEXTBOX_W-w)/2) + TEXTBOX_X, 248.35), position, font=font, fill="#40351d")

    @staticmethod
    def add_club(img: Image.Image, club_fp: str):
        club_logo = Image.open(club_fp)
        club_logo = resize_or_thumbnail(club_logo, (130, 130))
        pos = (60, 325)
        if club_logo.size[0] < 130:
            pos = (pos[0] + ((130 - club_logo.size[0])//2), pos[1])
        try:
            img.paste(club_logo, pos, mask=club_logo)
        except ValueError:
            img.paste(club_logo, pos)

    @staticmethod
    def add_country(img: Image.Image, country_fp: str):
        flag = Image.open(country_fp)
        flag = resize_or_thumbnail(flag, (130, 84))
        pos = (51, 498)
        if flag.size[0] < 130:
            pos = (pos[0] + ((130 - flag.size[0])//2), pos[1])
        try:
            img.paste(flag, pos, mask=flag)
        except ValueError:
            img.paste(flag, pos)

    @staticmethod
    def add_name(img: Image.Image, name: str):
        draw = ImageDraw.Draw(img)
        W, H = img.size
        font = ImageFont.truetype(
            "assets/fonts/CruyffSans-Bold.ecd5078c.otf", size=72
        )
        _, _, w, h = draw.textbbox(
            (0, 0),
            name,
            font=font,
            align="center",
        )
        draw.text(((W-w)/2, 681.07), name, font=font, fill="#40351d")

    @classmethod
    def create(cls, rarity: Rarity, color: Color, face_fp: str, overall: str, position: str, name: str, club_fp: str, country_fp: str):
        img = cls.create_base_card(rarity, color)
        cls.add_face(img, face_fp)
        cls.add_overall(img, overall)
        cls.add_position(img, position)
        cls.add_name(img, name)
        cls.add_club(img, club_fp)
        cls.add_country(img, country_fp)
        return img
