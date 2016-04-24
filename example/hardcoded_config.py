from config_interface import ConfigInterface

__all__ = [ "HardcodedConfig" ]

class HardcodedConfig(ConfigInterface):
    def __init__(self):
        self.board_size = 3
    
    def get_board_size(self):
        return self.board_size
