from design_components.button import *
from design_components.colors import MAINMENU_BUTTON_BACKGROUND_COLOR
from design_components.colors import MAINMENU_BUTTON_BACKGROUND_HOVER_COLOR
from design_components.colors import MAINMENU_BUTTON_TEXT_COLOR
from design_components.fonts import MAINMENU_BUTTON_FONT
from app.config import SCREEN_WIDTH, SCREEN_HEIGHT
from app.events import MAINMENU_BUTTON_CLICKED


class MainmenuButton(Button):
    def __init__(self):
        palette = ButtonPalette(
            MAINMENU_BUTTON_BACKGROUND_COLOR,
            MAINMENU_BUTTON_TEXT_COLOR,
            MAINMENU_BUTTON_BACKGROUND_HOVER_COLOR
        )
        position = ButtonPosition(
            SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 100, 50, 20
        )
        text = 'Let\'s die!'
        font = MAINMENU_BUTTON_FONT
        super().__init__(
            MAINMENU_BUTTON_CLICKED,
            text,
            font,
            palette,
            position
        )