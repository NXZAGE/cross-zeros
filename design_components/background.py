import pygame 
from design_components.colors import BACKGROUND_COLOR
from design_components.component import Component

class Background(Component):
    def __init__(self):
        self.__background_color = BACKGROUND_COLOR
        self.__logo_surface = pygame.image.load('assets/img/logo.png')
        self.__logo_surface = pygame.transform.scale(
            self.__logo_surface,
            (
                self.__logo_surface.get_width() // 10,
                self.__logo_surface.get_height() // 10
            ) 
        )
        self.__logo_rect = self.__logo_surface.get_rect(center=(100, 100))
        
    def display(self, screen):
        screen.fill(self.__background_color)
        screen.blit(self.__logo_surface, self.__logo_rect)