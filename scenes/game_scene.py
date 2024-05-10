from scenes.Scene import Scene
from app.bot import Bot
from design_components.game_field import GameField
from design_components.ticker import Ticker
from design_components.background import Background
from design_components.retry_button import RetryButton
from design_components.colors import BLOOD_COLOR
from app.events import *

class GameScene(Scene):
    def __init__(self, mode):
        super().__init__()
        self.__game_ended = False 
        self.__game_field = GameField()
        self.player = 0
        self.__components = [
            Background(),
            Ticker("kill yourself", BLOOD_COLOR, 2),
        ]    
        
        self.__retry_button = RetryButton()
        
        self.__bot = Bot(mode) 
        
    def check_end(self):
        if self.__game_ended: return
        if self.__game_field.cross_won():
            print("YOU WON")
            self.__game_ended = True
        if self.__game_field.zero_won():
            print("YOU LOSE")
            self.__game_ended = True 
        if self.__game_field.draw():
            print("DRAW")
            self.__game_ended = True 
            
        if self.__game_ended:
            self.__game_field.current_player = 0
        
        
        
    def display(self, screen):
        for component in self.__components:
            component.display(screen)
            
        self.__game_field.display(screen)
        
        if self.__game_ended:
            self.__retry_button.display(screen)
            
        
    def update(self, events):
        for component in self.__components:
            component.update(events)
            
        self.__game_field.update(events)
        
        if not self.__game_ended: self.check_end()
        if self.__game_field.current_player == -1:
            best_move = self.__bot.get_move(self.__game_field, )
            print(best_move)
            self.__game_field.cells[best_move[0]][best_move[1]].set_zero()
            print("computer moved")
            self.__game_field.current_player = 1
            self.check_end()
                
        if self.__game_ended:
            self.__retry_button.update(events)
            
        for event in events:
            if event == RETRY_BUUTON_CLICKED:
                pygame.event.post(ACTIVATE_LEVEL_SELECT_SCENE)
                
        
    