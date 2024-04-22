import pygame
from config import SCREEN_HEIGHT, SCREEN_WIDTH

class Core:
    def  __init__(self):
       self.__screen = pygame.display.set_mode(SCREEN_WIDTH, SCREEN_HEIGHT)
       self.__events = []
       self.__scenes = {}
       self.__is_running = False 
       self.__is_terminated = False 
       self.__current_scene = 1
       
    def update_events(self):
        self.events = pygame.event.get()
       
    def run(self):
        self.is_running = True 
        self.is_terminated = False 
    
    def stop(self):
        pass 
    
    