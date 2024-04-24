import pygame
from app.config import SCREEN_WIDTH, SCREEN_HEIGHT, FPS
from app.events import *
from scenes.end_game_scene import EndGameScene
from scenes.game_scene import GameScene
from scenes.level_select_scene import LevelSelectScene
from scenes.mainmenu_scene import MainmenuScene


class Core:
    def  __init__(self):
        pygame.init()
        self.__screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.__events = []
        self.__scenes = {}
        self.__is_running = False
        self.__is_terminated = False
        self.__current_scene = MainmenuScene()
        self.__clock = pygame.time.Clock()
        
    def run(self):
        print(pygame.font.get_fonts())
        self.is_running = True
        self.is_terminated = False
        while self.__is_terminated == False:
            self.__clock.tick(FPS)
            self.__update_events()
            self.__current_scene.update(self.__events)
            self.__current_scene.display(self.__screen)
            self.__check_termination()
            self.__check_scene_change()
            pygame.display.update()
    
    def stop(self):
        pass 
  
    def __update_events(self):
        self.__events = pygame.event.get()
        
    def __check_termination(self):
        for event in self.__events:
            if event.type == pygame.QUIT:
                self.__is_terminated = True
            
    def __check_scene_change(self):
        pass 
    
    
    