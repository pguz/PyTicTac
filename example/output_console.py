from output_interface import OutputInterface

__all__ = [ "OutputConsole" ]

class OutputConsole(OutputInterface):
    PLAYERS = ['_', 'X', 'O']
    
    def show_welcome(self):
        print("Welcome to Tic Tac game")

    def show_board(self, board):
        
        delimeter_size = board.shape[0] + 2
        
        self.delimeter(delimeter_size)
        print('')
        for row in board:
            print(' ', end = '')
            for elem in row:
                print(OutputConsole.PLAYERS[elem], end = '')
            print('')
        print('')
        self.delimeter(delimeter_size)

    def show_draw(self):
        print("It is a draw")

    def show_winner(self, player):
        print("Winner is: {0:d}!".format(player))
        
    def delimeter(self, size):
       print(size * '#')
