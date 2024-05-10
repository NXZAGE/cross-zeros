import pygame
from design_components.component import Component
from design_components.cell import Cell
from design_components.colors import BLOOD_COLOR, GREY_ACCENT_COLOR
from app.events import *

class Line:
    def __init__(self, cell1, cell2, cell3):
        self.cells = [cell1, cell2, cell3]
        
    def cross_won(self):
        result = self.cells[0].is_cross() and \
                 self.cells[1].is_cross() and \
                 self.cells[2].is_cross()
        return result
    
    def zero_won(self):
        result = self.cells[0].is_zero() and \
                 self.cells[1].is_zero() and \
                 self.cells[2].is_zero()
        return result
        

class GameField(Component):
    def __init__(self):
        x = 400
        y = 200
        shift = 200
        self.cells = [
            [
                Cell(CELL_00_CLICKED, x + shift * 0, y + shift * 0), 
                Cell(CELL_01_CLICKED, x + shift * 1, y + shift * 0), 
                Cell(CELL_02_CLICKED, x + shift * 2, y + shift * 0)
            ],
            [
                Cell(CELL_10_CLICKED, x + shift * 0, y + shift * 1), 
                Cell(CELL_11_CLICKED, x + shift * 1, y + shift * 1), 
                Cell(CELL_12_CLICKED, x + shift * 2, y + shift * 1)
            ],
            [
                Cell(CELL_20_CLICKED, x + shift * 0, y + shift * 2), 
                Cell(CELL_21_CLICKED, x + shift * 1, y + shift * 2), 
                Cell(CELL_22_CLICKED, x + shift * 2, y + shift * 2)
            ]
        ]
        
        self.__rect = pygame.Rect(x, y, shift * 3, shift * 3)
        self.__border_rect = self.__rect
        self.lines = []
        self.current_player = 1
        
    def update_lines(self):
        self.lines.clear()
        self.lines = [
            Line(self.cells[0][0], self.cells[0][1], self.cells[0][2]),
            Line(self.cells[1][0], self.cells[1][1], self.cells[1][2]),
            Line(self.cells[2][0], self.cells[2][1], self.cells[2][2]),
            Line(self.cells[0][0], self.cells[1][0], self.cells[2][0]),
            Line(self.cells[0][1], self.cells[1][1], self.cells[2][1]),
            Line(self.cells[0][2], self.cells[1][2], self.cells[2][2]),
            Line(self.cells[0][0], self.cells[1][1], self.cells[2][2]),
            Line(self.cells[2][0], self.cells[1][1], self.cells[0][2]),
        ]
        
    def cross_won(self):
        for line in self.lines:
            if line.cross_won(): return True 
        return False 
    
    def zero_won(self):
        for line in self.lines:
            if line.zero_won(): return True 
        return False 
    
    def draw(self):
        if self.cross_won() or self.zero_won(): return False
        for line in self.cells:
            for cell in line:
                if cell.is_blank(): return False 
                
        return True
    
    def update(self, events):
        for line in self.cells:
            for cell in line:
                cell.update(events)
                
        for event in events:
            if self.current_player == 1:
                if event == CELL_00_CLICKED:
                    if self.cells[0][0].is_blank() == False:
                        continue 
                    self.cells[0][0].set_cross()
                    self.current_player = -1
                    continue 
                if event == CELL_01_CLICKED:
                    if self.cells[0][1].is_blank() == False:
                        continue 
                    self.cells[0][1].set_cross()
                    self.current_player = -1
                    continue  
                if event == CELL_02_CLICKED:
                    if self.cells[0][2].is_blank() == False:
                        continue 
                    self.cells[0][2].set_cross()
                    self.current_player = -1
                    continue 
                if event == CELL_10_CLICKED:
                    if self.cells[1][0].is_blank() == False:
                        continue 
                    self.cells[1][0].set_cross()
                    self.current_player = -1
                    continue 
                if event == CELL_11_CLICKED:
                    if self.cells[1][1].is_blank() == False:
                        continue 
                    self.cells[1][1].set_cross()
                    self.current_player = -1
                    continue 
                if event == CELL_12_CLICKED:
                    if self.cells[1][2].is_blank() == False:
                        continue 
                    self.cells[1][2].set_cross()
                    self.current_player = -1
                    continue 
                if event == CELL_20_CLICKED:
                    if self.cells[2][0].is_blank() == False:
                        continue 
                    self.cells[2][0].set_cross()
                    self.current_player = -1
                    continue 
                if event == CELL_21_CLICKED:
                    if self.cells[2][1].is_blank() == False:
                        continue 
                    self.cells[2][1].set_cross()
                    self.current_player = -1
                    continue 
                if event == CELL_21_CLICKED:
                    if self.cells[2][1].is_blank() == False:
                        continue 
                    self.cells[2][1].set_cross()
                    self.current_player = -1
                    continue 
                if event == CELL_22_CLICKED:
                    if self.cells[2][2].is_blank() == False:
                        continue 
                    self.cells[2][2].set_cross()
                    self.current_player = -1
                    continue 
        
        self.update_lines()
            
    def display(self, screen):
        pygame.draw.rect(screen, GREY_ACCENT_COLOR, self.__rect)
        pygame.draw.rect(screen, (0, 0, 0), self.__border_rect, 6)
        
        for line in self.cells:
            for cell in line:
                cell.display(screen)