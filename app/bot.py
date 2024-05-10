import copy
from random import randint

class Bot:
    def __init__(self, mode):
        self.__mode = mode # 2 - imba, 1 - norm, 0 - random
        
    def get_move(self, gamefield):
        print("move requested")
        return self.minimax(gamefield, -1, 1)["ij"]
        
        
    def minimax(self, gamefield, current_player, depth): # obv, array with stats +-, 1/-1
        if gamefield.cross_won():
            return { "ij": (3, 3), "score": 10 - depth }
        if gamefield.zero_won():
            return { "ij": (3, 3), "score": depth - 10 } 
        if gamefield.draw():
            return { "ij": (3, 3), "score": 0 }
        
        
        available_moves = []
        cells = gamefield.cells
        for i in range(len(cells)):
            for j in range(len(cells[i])):
                if cells[i][j].is_blank():
                    available_moves.append((i, j))
                    
        if self.__mode == 0:
            return { "ij": available_moves[randint(0, len(available_moves) - 1)] }     
        
        moves = []
        for move_ij in available_moves:
            move = { 'ij': move_ij }
            if current_player == -1:
                gamefield.cells[move_ij[0]][move_ij[1]].set_zero()
            else:
                gamefield.cells[move_ij[0]][move_ij[1]].set_cross()
            gamefield.update_lines()
            move['score'] = self.minimax(gamefield, -current_player, depth + 1)["score"]
            gamefield.cells[move_ij[0]][move_ij[1]].set_blank()
            gamefield.update_lines()
            moves.append(move)
        
        # if depth == 0: 
        bestmove = moves[0]
        for move in moves:   
            if current_player == -1:
                if move["score"] <= bestmove["score"]:
                    bestmove = move
                # elif self.__mode == 1 and randint(0, 15) == 0:
                #     bestmove = move
            elif current_player == 1:
                if move["score"] >= bestmove["score"]:
                    bestmove = move
                elif self.__mode == 1 and randint(0, 14) == 0:
                    bestmove = move
                
        return bestmove
        # else:
        #     score = 0
        #     for move in moves:
        #         score += move["score"]
            
        #     return { "ij": (-1, -1), "score": score }
            
        