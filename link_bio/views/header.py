import reflex as rx
from link_bio.components.link_icon import link_icon
from link_bio.components.info_tex import info_text
from link_bio.components.title import title
from link_bio.styles.styles import Size as Size
from link_bio.styles.colors import TextColor as TextColor
from link_bio.styles.colors import Color as Color

def header(details=True)->rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.avatar(fallback="BM", src="/stitch.png",size="9", radius="full", bg=Color.CONTENT.value, color=TextColor.BODY.value, padding="2px", border="4px", border_color=Color.PRIMARY.value),
            rx.vstack(
                rx.heading("BRAIS MOURE"),
                rx.text("@mouredev", margin_top=Size.ZER0.value),
                rx.hstack(
                    link_icon("https://x.com/mouredev"),
                    link_icon("https://x.com/mouredev"),
                    link_icon("https://x.com/mouredev")
                ),        
            ),
            spacing="7"
        ),
        rx.cond(
            details,
            rx.vstack(
                rx.flex(
                    info_text("+13", "años de experiencia"),
                    rx.spacer(),
                    info_text("100+", "aplicaciones creadas"),
                    rx.spacer(),
                    info_text("1M+", "seguidores"),
                    width="100%"
                ),
               rx.text("""MoureDev es el reflejo de mi ilusión por crecer como profesional dentro de la industria del desarrollo del software.
                Como freelance, me he especializado en desarrollo de aplicaciones iOS, Android y web.""", font_size=Size.DEFAULT.value ,color=TextColor.BODY.value),
        spacing="7"
                
            ),
        ),
   
    )