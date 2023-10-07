# UTCardMakr

- [UTCardMakr](#utcardmakr)
  - [Installation](#installation)
  - [Usage](#usage)

## Installation

```sh
pip install git+https://github.com/anasouh/utcardmakr
```

## Usage

```py
from utcardmakr import create_card, Rarity, Color

img = create_card(
    rarity=Rarity.RARE,
    color=Color.GOLD, 
    face_fp="player/face/path", 
    overall="84", 
    position="RB", 
    name="Hakimi", 
    club_fp="club/logo/path", 
    country_fp="flag/icon/path"
)

# Show the result
img.show()

# Save the result
img.save("card.png")
```