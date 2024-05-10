from design_components.button import *
from design_components.colors import MAINMENU_BUTTON_BACKGROUND_COLOR
from design_components.colors import MAINMENU_BUTTON_BACKGROUND_HOVER_COLOR
from design_components.colors import MAINMENU_BUTTON_TEXT_COLOR
from design_components.fonts import RETRY_BUTTON_FONT
from app.config import SCREEN_WIDTH, SCREEN_HEIGHT
from app.events import RETRY_BUUTON_CLICKED


class RetryButton(Button):
    def __init__(self):
        palette = ButtonPalette(
            MAINMENU_BUTTON_BACKGROUND_COLOR,
            MAINMENU_BUTTON_TEXT_COLOR,
            MAINMENU_BUTTON_BACKGROUND_HOVER_COLOR
        )
        position = ButtonPosition(
            200, 500, 50, 20
        )
        text = 'Retry'
        font = RETRY_BUTTON_FONT
        super().__init__(
            RETRY_BUUTON_CLICKED,
            text,
            font,
            palette,
            position
        )