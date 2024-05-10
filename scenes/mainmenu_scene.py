import pygame
from scenes.Scene import Scene 
from design_components.background import Background
from design_components.ticker import Ticker
from design_components.mainmenu_button import MainmenuButton
from design_components.colors import *
from app.events import MAINMENU_BUTTON_CLICKED, ACTIVATE_LEVEL_SELECT_SCENE


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
         
        for event in events:
            if event == MAINMENU_BUTTON_CLICKED:
                pygame.event.post(ACTIVATE_LEVEL_SELECT_SCENE)
    