from PIL import Image, ImageDraw, ImageFont
from utcardmakr.const import *
from utcardmakr.ctypes.Card import Card
from utcardmakr.utils import *

class LargeCard(Card):

    @staticmethod
    def create_base_card(rarity: Rarity, color: Color):
        img = Image.new("RGBA", (676, 1025), (0, 0, 0, 0))
        card_bg = Image.open(CARD_BG[rarity.value][color.value])
        card_bg = card_bg.resize((676, 1025))
        img.paste(card_bg, (0, 0))
        return img

    @staticmethod
    def add_face(img: Image.Image, face_fp: str):
        face = Image.open(face_fp)
        pos = (110, 133)
        MAX_WIDTH = 544
        height = 550
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
            (50, 147),
            overall,
            fill="#40351d",
            font=ImageFont.truetype(
                get_font_fp("assets/fonts/condensed/Numbers-Bold.ttf"), size=124
            ),
            align="center",
        )

    @staticmethod
    def add_position(img: Image.Image, position: str):
        draw = ImageDraw.Draw(img)
        TEXTBOX_W = 120
        TEXTBOX_X = 50
        font = ImageFont.truetype(
            get_font_fp("assets/fonts/condensed/CruyffSansCondensed+DINArabic+SSTThai-Regular.otf"), size=56
        )
        _, _, w, h = draw.textbbox(
            (0, 0),
            position,
            font=font,
            align="center",
        )
        draw.text((((TEXTBOX_W-w)/2) + TEXTBOX_X, 272), position, font=font, fill="#40351d")

    @staticmethod
    def add_club(img: Image.Image, club_fp: str):
        club_logo = Image.open(club_fp)
        club_logo = resize_or_thumbnail(club_logo, (59, 59))
        pos = (395, 904)
        if club_logo.size[0] < 59:
            pos = (pos[0] + ((59 - club_logo.size[0])//2), pos[1])
        try:
            img.paste(club_logo, pos, mask=club_logo)
        except ValueError:
            img.paste(club_logo, pos)
            
    @staticmethod
    def add_league(img: Image.Image, league_fp: str):
        league_logo = Image.open(league_fp)
        league_logo = resize_or_thumbnail(league_logo, (59, 59))
        pos = (309, 904)
        if league_logo.size[0] < 59:
            pos = (pos[0] + ((59 - league_logo.size[0])//2), pos[1])
        try:
            img.paste(league_logo, pos, mask=league_logo)
        except ValueError:
            img.paste(league_logo, pos)

    @staticmethod
    def add_country(img: Image.Image, country_fp: str):
        flag = Image.open(country_fp)
        flag = resize_or_thumbnail(flag, (64, 39))
        pos = (221, 913)
        if flag.size[0] < 64:
            pos = (pos[0] + ((64 - flag.size[0])//2), pos[1])
        try:
            img.paste(flag, pos, mask=flag)
        except ValueError:
            img.paste(flag, pos)

    @staticmethod
    def add_name(img: Image.Image, name: str):
        draw = ImageDraw.Draw(img)
        W, H = img.size
        font = ImageFont.truetype(
            get_font_fp("assets/fonts/CruyffSans-Bold.ecd5078c.otf"), size=72
        )
        _, _, w, h = draw.textbbox(
            (0, 0),
            name,
            font=font,
            align="center",
        )
        draw.text(((W-w)/2, 693), name, font=font, fill="#40351d")

    @staticmethod
    def create_attribute(name: str, avg: str) -> Image.Image:
        img = Image.new("RGBA", (83, 100), (0, 0, 0, 0))
        draw = ImageDraw.Draw(img)
        font_fp = get_font_fp("assets/fonts/condensed/CruyffSansCondensed+DINArabic+SSTThai-Medium.otf")
        font = ImageFont.truetype(font_fp, size=38)
        _, _, w, h = draw.textbbox(
            (0, 0),
            name,
            font=font,
            align="center",
        )
        draw.text(((83-w)/2, 0), name, font=font, fill="#40351d")
        font = ImageFont.truetype(font_fp, size=59)
        _, _, w, h = draw.textbbox(
            (0, 0),
            avg,
            font=font,
            align="center",
        )
        draw.text(((83-w)/2, 46), avg, font=font, fill="#40351d")
        return img
    
    @classmethod
    def add_attributes(cls, img: Image.Image, *attributes: str):
        NAMES = ("PAC", "SHO", "PAS", "DRI", "DEF", "PHY")
        pos = (54, 785)
        spacing = 46
        for name, value in zip(NAMES, attributes):
            attr = cls.create_attribute(name, value)
            img.paste(attr, pos, mask=attr)
            pos = (pos[0] + spacing + 51, pos[1])

    @classmethod
    def create(cls, rarity: Rarity, color: Color, face_fp: str, overall: str, position: str, name: str, club_fp: str, league_fp: str, country_fp: str, attributes: tuple[str, str, str, str, str, str]):
        if len(attributes) != 6:
            raise ValueError("attributes must be a tuple of 6 strings")
        img = cls.create_base_card(rarity, color)
        cls.add_face(img, face_fp)
        cls.add_overall(img, overall)
        cls.add_position(img, position)
        cls.add_name(img, name)
        cls.add_club(img, club_fp)
        cls.add_league(img, league_fp)
        cls.add_country(img, country_fp)
        cls.add_attributes(img, *attributes)
        return img
