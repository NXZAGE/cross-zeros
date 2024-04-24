import pygame 

ACTIVATE_MAIN_MENU_SCENE = pygame.event.Event(pygame.USEREVENT + 1)
ACTIVATE_LEVEL_SELECT_SCENE = pygame.event.Event(pygame.USEREVENT + 2)
ACTIVATE_GAME_SCENE = pygame.event.Event(pygame.USEREVENT + 3)
MAINMENU_BUTTON_CLICKED = pygame.event.Event(pygame.USEREVENT + 4)