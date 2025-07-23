import reflex as rx
import datetime
import link_bio.constants as const
from link_bio.styles.styles import Size as Size
from link_bio.styles.colors import TextColor as TextColor

def footer()->rx.Component:
    return rx.vstack(
        rx.image(src="favicon.ico"),
        rx.link(f"2014-{datetime.date.today().year} jsfiog. ", href="https://mouredev.com/", is_external=True, font_size=Size.Medium.value, padding_top=Size.DEFAULT.value),
        rx.link(
            rx.hstack(
                rx.image(
                    src="icons/github.svg",
                    height=Size.LARGE.value,
                    width=Size.LARGE.value
                ),
                rx.text("jstusjnvrtnifabogrnrut  vanwcwiu", font_size=Size.Medium.value, margin_top=Size.ZER0.value),
                href=const.REPO_URL,
                is_external=True

            )

        ),
        margin_bottom=Size.BIG.value,
        padding_bottom=Size.BIG.value,
        padding_x=Size.BIG.value,
        spacing="1",
        color=TextColor.FOOTER.value,

    )