from enum import Enum
import reflex as rx
from .colors import Color as Color
from .colors import TextColor as TextColor
from .fonts import Font as Font

MAX_WIDTH="600px"

class Size(Enum):
    ZER0="0px !import"
    SMALL="0.5em"
    Medium="0.8em"
    DEFAULT="1em"
    LARGE="1.5EM"
    BIG="2em"
    VERY_BIG="4em"

class Spacing(Enum):
    ZERO = "0"
    VERY_SMALL = "1"
    SMALL = "3"
    DEFAULT = "4"
    LARGE = "5"
    BIG = "6"
    MEDIUM_BIG = "7"
    VERY_BIG = "9"

BASE_STYLE={
    "font-family":Font.DEFAULT.value,
    "background_color":Color.BACKGROUND.value,
    rx.heading: {
        "color":TextColor.HEADER.value,
        "font-family":Font.Title.value
    },
    rx.button:{
        "width":"100%",
        "height": "100%",
        "padding": Size.SMALL.value,
        "border_radius": Size.DEFAULT.value,
        "color":TextColor.HEADER.value,
        "background_color":Color.CONTENT.value,
        "white_space": "normal",
        "text_align":"start",
        "_hover":{
            "background_color":Color.SECONDARY.value
        }
    }
}

navbar_title_style=dict(
    font_family=Font.DEFAULT.value,
    font_size=Size.LARGE.value
)

title_style=dict(
    width="100%",
    padding_top=Size.DEFAULT.value,
    
)

button_title_style= dict(
    font_family=Font.Title.value,
    font_size=Size.DEFAULT.value,
    color=TextColor.HEADER.value
)

button_body_style= dict(
    font_size=Size.Medium.value,
    color=TextColor.BODY.value
)