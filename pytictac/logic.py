import numpy as np

from board import Board 

__all__ = [ "Logic" ]

class Logic():    
    NUM_PLAYERS = 2
    
    def __init__(self, boardSize):
        self._board = Board(boardSize, Logic.NUM_PLAYERS)
        self._board_size = boardSize
        self._turn = 1
        self._end = False
        self._winner = None # None, PLAYER1, PLAYER2
        
    def get_board(self):
        return self._board.get()
        
    def get_player(self):
        return self._turn - 1
        
    def if_end(self):
        return self._end
        
    def get_winner(self):
        return self._winner
    
    def make_move(self, x, y):
        if not 0 <= x < self._board_size:
            raise ValueError("Unproper x coord")
        if not 0 <= y < self._board_size:
            raise ValueError("Unproper y coord")

        if self._end:
            return False
            
        if not self._board.put(self._turn, x, y):
            return False
        
        if self.check_winner():
            self._winner = self._turn
            self._end = True
            return True
            
        if not self._board.if_empty_place():
            self._end = True
            return True
            
        self.change_player()
        
        return True
    
    def change_player(self):
        self._turn = self._turn % Logic.NUM_PLAYERS + 1
            
    def check_winner(self):
        board = self._board.get()
        return self.check_rows(board) or self.check_cols(board)
    
    def check_rows(self, board):
        return True in np.all(board == self._turn, axis = 0)
        
    def check_cols(self, board):
        return True in np.all(board == self._turn, axis = 1)
