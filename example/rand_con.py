from hardcoded_config import HardcodedConfig 
from input_random import InputRandom 
from output_console import OutputConsole 
from game import Game 

def main():
    
    # CONFIG
    game_config = HardcodedConfig()
    
    # INPUT
    input_random1 = InputRandom(game_config.get_board_size())
    input_random2 = InputRandom(game_config.get_board_size())
    game_input = [ input_random1, input_random2 ]
    
    # OUTPUT
    output_console = OutputConsole()
    game_output = output_console

    # GAME
    game = Game(game_config, game_input, game_output)
    game.run()

if __name__ == '__main__':
    main()
