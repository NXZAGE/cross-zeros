from scenes.Scene import Scene 
from design_components.background import Background
from design_components.ticker import Ticker
from design_components.easy_level_button import EasyLevelButton
from design_components.norm_level_button import NormLevelButton
from design_components.hard_level_button import HardLevelButton
from design_components.colors import *
from app.events import *

class LevelSelectScene(Scene):
    def __init__(self):
        super().__init__()
        self.__components = [
                Background(),
                Ticker("select", BLOOD_COLOR, 4),
                EasyLevelButton(),
                NormLevelButton(),
                HardLevelButton()
            ]
        
    def display(self, screen):
        for component in self.__components:
            component.display(screen)
        
    def update(self, events):
        for component in self.__components:
            component.update(events)
    