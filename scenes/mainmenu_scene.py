from scenes.Scene import Scene 
from design_components.background import Background
from design_components.ticker import Ticker
from design_components.mainmenu_button import MainmenuButton
from design_components.colors import *


class MainmenuScene(Scene):
    def __init__(self):
        super().__init__()
        self.__components = [
            Background(),
            Ticker('Death.', BLOOD_COLOR, 4),
            MainmenuButton()
        ]

    def display(self, screen):
        for component in self.__components:
            component.display(screen)

    def update(self, events):
        for component in self.__components:
            component.update(events)
        pass 
    