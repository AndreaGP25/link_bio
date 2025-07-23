import reflex as rx
from link_bio.styles.colors import Color

class FloatButoon(rx.Component):
    library="antd"
    tag="FloatButton"
    icon="HeartOutlined"
    href="https://"
    target="_blank"
    badge= {"dot": True, "color": Color.PRIMARY.value}


float_button=FloatButoon.create

