import pygame
from design_components.component import Component

class Cell(Component):
    def __init__(self, activation_event, left = 0, top = 0):
        super().__init__()
        size = 200
        padding = 20
        self.__status = 0
        self.__activation_event = activation_event
        self.__cross_surface = pygame.image.load("assets/img/pentagram.png")
        self.__zero_surface = pygame.image.load("assets/img/coin.png")
        self.__cross_surface = pygame.transform.scale(self.__cross_surface, (size - 2 * padding, size - 2 * padding))
        self.__zero_surface = pygame.transform.scale(self.__zero_surface, (size - 2 * padding, size - 2 * padding))
        self.__rect = pygame.Rect(left, top, size, size)
        self.__border_rect = self.__rect
        self.__rect = self.__rect.move(padding, padding)
        
    def set_cross(self):
        self.__status = 1
                
    def set_zero(self):
        self.__status = -1
        
    def set_blank(self):
        self.__status = 0
        
    def is_cross(self):
        return self.__status == 1
    
    def is_zero(self):
        return self.__status == -1 
    
    def is_blank(self):
        return self.__status == 0
    
    def update(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.__border_rect.collidepoint(event.pos):
                    pygame.event.post(self.__activation_event)
                    print(f"cell {self.__activation_event.type} pressed")
    
    def display(self, screen):
        pygame.draw.rect(screen, (0, 0, 0), self.__border_rect, 3)
        if (self.__status == 0):
            return
        
        surface = self.__cross_surface if self.__status == 1 else self.__zero_surface
        screen.blit(surface, self.__rect)