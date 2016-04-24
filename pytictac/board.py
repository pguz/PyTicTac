import numpy as np

__all__ = [ "Board" ]

class Board():
    def __init__(self, size, num_fields):
        self._size = size
        self._num_fields = num_fields
        self._board = np.zeros((size, size), dtype = np.int)
    
    def get(self):
        return np.copy(self._board)
    
    def put(self, field, x, y):
        if not field - 1 in range(self._num_fields):
            raise ValueError("Unproper field value")
        if not 0 <= x < self._size:
            raise ValueError("Unproper x coord")
        if not 0 <= y < self._size:
            raise ValueError("Unproper y coord")
        if self._board[x][y]:
            return False

        self._board[x][y] = field
        return True
        
    def if_empty_place(self):
        return 0 in self._board
