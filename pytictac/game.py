from logic import Logic 

__all__ = [ "Game" ]

class Game:
    def __init__(self, config, inputs, output):
        self._inputs = inputs
        self._output = output
        self._logic = Logic(config.get_board_size())
        
    def run(self):
        self._output.show_welcome()
        
        while True:
            
            self._output.show_board(self._logic.get_board())
            self.make_move()
            if not self._logic.if_end():
                continue

            # END OF GAME            
            self._output.show_board(self._logic.get_board())
            w = self._logic.get_winner()
            if w is None:
                # DRAW.
                self._output.show_draw()
            else:
                self._output.show_winner(w)
                
            break
            
    def make_move(self):
        player = self._logic.get_player()
            
        while True:
            x, y = self._inputs[player].get_move()
            if self._logic.make_move(x, y) is False:
                self._output.show_move_error(player)
                continue
            
            break
