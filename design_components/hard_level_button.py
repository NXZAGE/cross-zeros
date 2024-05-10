from design_components.button import *
from design_components.colors import MAINMENU_BUTTON_BACKGROUND_COLOR
from design_components.colors import MAINMENU_BUTTON_BACKGROUND_HOVER_COLOR
from design_components.colors import MAINMENU_BUTTON_TEXT_COLOR
from design_components.fonts import LEVEL_BUTTON_FONT
from app.config import SCREEN_WIDTH, SCREEN_HEIGHT
from app.events import DIFFICULTY_2_SELECTED


class HardLevelButton(Button):
    def __init__(self):
        palette = ButtonPalette(
            MAINMENU_BUTTON_BACKGROUND_COLOR,
            MAINMENU_BUTTON_TEXT_COLOR,
            MAINMENU_BUTTON_BACKGROUND_HOVER_COLOR
        )
        position = ButtonPosition(
            700, 700, 70, 20
        )
        text = 'Hard'
        font = LEVEL_BUTTON_FONT
        super().__init__(
            DIFFICULTY_2_SELECTED,
            text,
            font,
            palette,
            position
        )