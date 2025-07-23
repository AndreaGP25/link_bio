import reflex as rx
from link_bio.routes import Route
import link_bio.constants as const
from link_bio.components.link_button import link_button
from link_bio.components.title import title

def courses_links()->rx.Component:
    return rx.vstack(
        title("Cursos gratis"),
        link_button("Retos de programación", "Directos de lunes a viernes", "/icons/twitch-brands.svg" ,"https://www.twitch.tv/"),
        link_button("PYthon", "Tutoriales semanales","/icons/twitch-brands.svg", "https://www.youtube.com/"),
        link_button("SQL", "Tutoriales semanales", "/icons/twitch-brands.svg","https://www.youtube.com/"),
        link_button("Git", "El chat de la comunidad", "/icons/twitch-brands.svg", "https://discord.com/"),

        

        width="100%",
        spacing="4"
    )