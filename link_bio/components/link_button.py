import reflex as rx
import link_bio.styles.styles as styles
from link_bio.styles.styles import Size as Size

def link_button(title:str, body:str, image:str, url:str, is_external=True)->rx.Component:
    return rx.link(
        rx.button(
            rx.hstack(
                rx.image(src=image, width=Size.BIG.value, height=Size.BIG.value, margin=Size.Medium.value),
                rx.vstack(
                    rx.text(title, style=styles.button_title_style),
                    rx.text(body, style=styles.button_body_style),
                    spacing="1",
                    margin=Size.SMALL.value,
                    padding_right=Size.SMALL.value
                ),
                width="100%"
            )
        ),
        href=url,
        width="100%",
        
    )


    