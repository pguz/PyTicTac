from random import randint

from input_interface import InputInterface

__all__ = [ "InputRandom" ]

class InputRandom(InputInterface):
    
    def __init__(self, size):
        self._range = size - 1
    
    def get_move(self):
        return randint(0, self._range), randint(0, self._range) 
