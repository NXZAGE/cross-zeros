import pygame 

ACTIVATE_MAIN_MENU_SCENE = pygame.event.Event(pygame.USEREVENT + 1)
ACTIVATE_LEVEL_SELECT_SCENE = pygame.event.Event(pygame.USEREVENT + 2)
ACTIVATE_GAME_SCENE = pygame.event.Event(pygame.USEREVENT + 3)
MAINMENU_BUTTON_CLICKED = pygame.event.Event(pygame.USEREVENT + 4)

CELL_00_CLICKED = pygame.event.Event(pygame.USEREVENT + 5)
CELL_01_CLICKED = pygame.event.Event(pygame.USEREVENT + 6)
CELL_02_CLICKED = pygame.event.Event(pygame.USEREVENT + 7)
CELL_10_CLICKED = pygame.event.Event(pygame.USEREVENT + 8)
CELL_11_CLICKED = pygame.event.Event(pygame.USEREVENT + 9)
CELL_12_CLICKED = pygame.event.Event(pygame.USEREVENT + 10)
CELL_20_CLICKED = pygame.event.Event(pygame.USEREVENT + 11)
CELL_21_CLICKED = pygame.event.Event(pygame.USEREVENT + 12)
CELL_22_CLICKED = pygame.event.Event(pygame.USEREVENT + 13)

PLAYER_MOVED = pygame.event.Event(pygame.USEREVENT + 14)

RETRY_BUUTON_CLICKED = pygame.event.Event(pygame.USEREVENT + 15)

DIFFICULTY_0_SELECTED = pygame.event.Event(pygame.USEREVENT + 16)
DIFFICULTY_1_SELECTED = pygame.event.Event(pygame.USEREVENT + 17)
DIFFICULTY_2_SELECTED = pygame.event.Event(pygame.USEREVENT + 18)