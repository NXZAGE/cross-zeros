import pygame
from app.config import SCREEN_WIDTH, SCREEN_HEIGHT
from design_components.component import Component
from design_components.fonts import TICKER_FONT


class Ticker(Component):
    def __init__(self, text, text_color, count):
        super().__init__()
        self.__count = count
        font = TICKER_FONT
        self.__surface = font.render(text, True, text_color)
        rect = self.__surface.get_rect(
            bottomleft=(0, SCREEN_HEIGHT)
        )
        spacing = (SCREEN_WIDTH - count * self.__surface.get_width()) // count
        self.__rects = [rect.move(spacing // 2, 0)]
        self.__speed = 2
        
        for _ in range(count - 1):
            rect = self.__rects[-1].move(spacing, 0)
            rect.move_ip(rect.width, 0)
            self.__rects.append(rect)
        
    def update(self, events):
        for rect in self.__rects:
            rect.move_ip(self.__speed, 0)
            
        if self.__count == len(self.__rects) and self.__rects[-1].right >= SCREEN_WIDTH:
            last_rect = self.__rects[-1]
            new_rect = last_rect.move(-SCREEN_WIDTH, 0)
            self.__rects.insert(0, new_rect)
            
        if self.__count == len(self.__rects) - 1 and self.__rects[-1].left >=SCREEN_WIDTH:
            self.__rects.pop()
            
        
    def display(self, screen):
        for rect in self.__rects:
            screen.blit(self.__surface, rect)
        