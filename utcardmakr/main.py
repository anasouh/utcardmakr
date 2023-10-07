from PIL import Image, ImageDraw, ImageFont
from const import *

def resize_or_thumbnail(img: Image, size: tuple):
    if img.size[0] > size[0] or img.size[1] > size[1]:
        img.thumbnail(size)
    else:
        img = img.resize(size)
    return img

#  Create a new image 726x897 and make the card_bg cover it
def create_base_card(rarity: Rarity, color: Color):
    img = Image.new("RGBA", (726, 897), (0, 0, 0, 0))
    card_bg = Image.open(CARD_BG_SMALL[rarity.value][color.value])
    card_bg = card_bg.resize((726, 897))
    img.paste(card_bg, (0, 0))
    return img

#  Paste the face on the card size: 482x529, on position 184x139
def add_face(img: Image, face_fp: str):
    face = Image.open(face_fp)
    face = resize_or_thumbnail(face, (482, 529))
    try:
        img.paste(face, (184, 139), mask=face)
    except ValueError:
        img.paste(face, (184, 139))

# Create text "82" with the font "cards/fonts/condensed/CruyffSansCondensed+DINArabic+SSTThai-Bold.otf"
# Size: 124,09 pt, color: #40351d, position: 44,91x122,76px
def add_overall(img: Image, overall: str):
    draw = ImageDraw.Draw(img)
    draw.text(
        (44.91, 122.76),
        overall,
        fill="#40351d",
        font=ImageFont.truetype(
            "fonts/condensed/Numbers-Bold.ttf", size=124
        ),
        align="center",
    )

# Create text "ST" with the font "cards/fonts/condensed/CruyffSansCondensed+DINArabic+SSTThai-Regular.otf"
# Size: 56,77 pt, color: #40351d, position: 82,84x248,35px
def add_position(img: Image, position: str):
    draw = ImageDraw.Draw(img)
    draw.text(
        (82.84, 248.35),
        position,
        fill="#40351d",
        font=ImageFont.truetype(
            "fonts/condensed/CruyffSansCondensed+DINArabic+SSTThai-Regular.otf", size=56
        ),
        align="center",
    )

# Add the club logo size: 130x130, position: 60x325
def add_club(img: Image, club_fp: str):
    club_logo = Image.open(club_fp)
    club_logo = resize_or_thumbnail(club_logo, (130, 130))
    try:
        img.paste(club_logo, (60, 325), mask=club_logo)
    except ValueError:
        img.paste(club_logo, (60, 325))

# Add the country logo size: 118x72, position: 51x498
def add_country(img: Image, country_fp: str):
    flag = Image.open(country_fp)
    flag = resize_or_thumbnail(flag, (130, 84))
    try:
        img.paste(flag, (51, 498), mask=flag)
    except ValueError:
        img.paste(flag, (51, 498))

# Add the player name with the font "cards/fonts/CruyffSans-Bold.ecd5078c.otf" size: 72,15 pt, color: #40351d, position: 258.65x681.07px
def add_name(img: Image, name: str):
    draw = ImageDraw.Draw(img)
    draw.text(
        (258.65, 681.07),
        name,
        fill="#40351d",
        font=ImageFont.truetype(
            "fonts/CruyffSans-Bold.ecd5078c.otf", size=72
        ),
        align="center",
    )

def create_card(rarity: Rarity, color: Color, face_fp: str, overall: str, position: str, name: str, club_fp: str, country_fp: str):
    img = create_base_card(rarity, color)
    add_face(img, face_fp)
    add_overall(img, overall)
    add_position(img, position)
    add_name(img, name)
    add_club(img, club_fp)
    add_country(img, country_fp)
    return img
