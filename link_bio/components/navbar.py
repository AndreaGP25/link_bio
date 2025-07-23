import reflex as rx
from link_bio.routes import Route
from link_bio.styles.styles import Size as Size
from link_bio.styles.colors import Color as Color
import link_bio.styles.styles as styles
from link_bio.components.ant_components import float_button

def navbar()->rx.Component:
    return rx.hstack(
        rx.link(
            rx.box(
            rx.el.span("moure", color=Color.PRIMARY.value),
            rx.el.span("dev", color=Color.SECONDARY.value),
            style=styles.navbar_title_style
            ),
        href=Route.INDEX.value
        ),
        float_button(),
        position="sticky",
        bg=Color.CONTENT.value,
        padding_x=Size.DEFAULT.value,
        padding_y=Size.SMALL.value,
        z_index="999",
        top="0"
    )