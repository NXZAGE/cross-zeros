import pygame

class ButtonPalette:
    def __init__(self, background, text, hover):
        self.background = background
        self.text = text 
        self.hover = hover
    
    
class ButtonPosition:
    def __init__(self, left, top, paddingX, paddingY):
        self.left = left
        self.top = top
        self.paddingX = paddingX 
        self.paddingY = paddingY 
        
  
class ButtonBorder:
    def __init__(self, size, radiuce, color):
        self.size = size 
        self.radiuce = radiuce
        self.color = color


class Button:
    def __init__(self, event, text, font, palette, position, border=None):
        self.__activation_event = event
        self.palette = palette
        self.current_background_color = palette.background
        self.__text_surface = font.render(text, True, palette.text)
        self.__text_rect = pygame.Rect(
            position.left - self.__text_surface.get_width() // 2,
            position.top - self.__text_surface.get_height() // 2,
            self.__text_surface.get_width(),
            self.__text_surface.get_height()
        )
        self.__rect = pygame.Rect(
            position.left - self.__text_surface.get_width() // 2 - position.paddingX,
            position.top - self.__text_surface.get_height() // 2 - position.paddingY,
            self.__text_surface.get_width() + position.paddingX * 2,
            self.__text_surface.get_height() + position.paddingY * 2
        )
        
    def update(self, events):
        for event in events:
            if event.type == pygame.MOUSEMOTION:
                if self.__rect.collidepoint(event.pos):
                    self.current_background_color = self.palette.hover 
                else:
                    self.current_background_color = self.palette.background
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.__rect.collidepoint(event.pos):
                    pygame.event.post(self.__activation_event)
                    print("button pressed")
                    
    def display(self, screen):
        pygame.draw.rect(
            screen, self.current_background_color, self.__rect
        )
        screen.blit(self.__text_surface, self.__text_rect)
        
        