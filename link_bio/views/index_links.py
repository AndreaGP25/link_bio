import reflex as rx
from link_bio.routes import Route
import link_bio.constants as const
from link_bio.components.link_button import link_button
from link_bio.components.title import title

def index_links()->rx.Component:
    return rx.vstack(
        title("Comunidad"),
        link_button("Twitch", "Directos de lunes a viernes", "/icons/twitch-brands.svg" ,"https://www.twitch.tv/"),
        link_button("Youtube", "Tutoriales semanales","/icons/twitch-brands.svg", "https://www.youtube.com/"),
        link_button("YouTube (canal secundario)", "Tutoriales semanales", "/icons/twitch-brands.svg","https://www.youtube.com/"),
        link_button("Discord", "El chat de la comunidad", "/icons/twitch-brands.svg", "https://discord.com/"),
        link_button("Cursos gratis", "Ejercicios semanales", "/icons/twitch-brands.svg", Route.COURSES.value, False),

        title("Recursos y más"),
        link_button("Twitch", "Directos de lunes a viernes", "/icons/twitch-brands.svg","https://www.twitch.tv/"),
        link_button("Youtube", "Tutoriales semanales", "/icons/twitch-brands.svg", "https://www.youtube.com/"),
        link_button("YouTube (canal secundario)", "Tutoriales semanales", "/icons/twitch-brands.svg", "https://www.youtube.com/"),
        link_button("Discord", "El chat de la comunidad", "/icons/twitch-brands.svg", "https://discord.com/"),

        title("Contacto"),
        link_button("Mi publicInbox", "Tutoriales semanales", "/icons/twitch-brands.svg","https://www.youtube.com/"),
        link_button("Invítame un café", "El chat de la comunidad", "/icons/twitch-brands.svg","https://discord.com/"),

        width="100%",
        spacing="4"
    )