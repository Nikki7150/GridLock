from player import HumanPlayer 
from player import RandomComputerPlayer
from player import GeniusComputerPlayer
import time

class TicTacToe:
    def __init__(self): 
        self.board = [' ' for _ in range(9)] # we will use a single list to rep 3x3 board
        self.current_winner = None # keep track of winner
        self.winning_cells = [] # keep track of winning cells

    def print_board(self):
        # this is just getting the rows
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]: # indexing into length 9 list, i in range 3 - which group of three spaces are we choosing - represents row
            print('| ' + ' | '.join(row) + ' |')


    @staticmethod
    def print_board_nums(): #static becasue we dont have to pass in a board and dont have to use self
        #  0 | 1 | 2 etc (tells us what number corresponds to what box)
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']
        #for (i, spot) in enumerate(self.board): # create a list and assign tuples that have index, value at that index
        # ['x', 'x', 'o'] -> [(0, 'x'), (1, 'x'), (2, 'o')]
        #if spot == ' ':
        #    moves.append(i) # want to know which sopaces
        #return moves

    def empty_squares(self):
        return ' ' in self.board
    
    def num_empty_squares(self):
        # return len(self.available_moves()) or
        return self.board.count(' ')
    
    def make_move(self, square, letter):
        # if valid move, then make the move (assign square to letter)
        # then return true. If invalid, return false
        if self.board[square] == ' ':
            self.board[square] = letter
            winning_combo = self.winner(square, letter)
            if winning_combo: 
                self.current_winner = letter
                self.winning_cells = winning_combo
            return True
        return False
    
    def winner(self, square, letter):
        # winner if 3 in a row anywhere.. we have to check all of these!
        # check the row
        row_ind = square // 3
        row_indices = [row_ind*3, row_ind*3+1, row_ind*3+2]
        row = [self.board[i] for i in row_indices]
        if all([spot == letter for spot in row]):
            return row_indices
        
        # check column
        col_ind = square % 3
        col_indices = [col_ind+i*3 for i in range(3)]
        column = [self.board[i] for i in col_indices]
        if all([spot == letter for spot in column]):
            return col_indices
        
        # check diagonals
        # only if the square is an even number (0, 2, 4, 6, 8) - 
        # these are the only moves possible to win a diagonal
        if square % 2 == 0:
            diagonal1_indices = [0, 4, 8]
            diagonal1 = [self.board[i] for i in diagonal1_indices] # left to right diagonal
            if all([spot == letter for spot in diagonal1]):
                return diagonal1_indices
            
            diagonal2_indices = [2, 4, 6]
            diagonal2 = [self.board[i] for i in diagonal2_indices] # right to left diagonal
            if all([spot == letter for spot in diagonal2]):
                return diagonal2_indices
            
        # if all of these fail
        return None


def play(game, x_player, o_player, print_game=True):
    # returns the winner of the game (the letter)! or None for a tie
    if print_game:
        game.print_board_nums()

    letter = 'X' # starting letter
    # iterate while game still has empty squares
    # (we dont have to worry about winner because we'll just return that 
    # which breaks the loop)

    while game.empty_squares():
        # get the move from appropriate player
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)
        
        # function to make a move
        if game.make_move(square, letter):
            if print_game:
                print(letter + f' makes a move to square {square}')
                game.print_board()
                print('') # just empty line

            if game.current_winner:
                if print_game:
                    print(letter + ' wins!')
                return letter
            
            # after we made our move, we need to alternate letters
            letter = 'O' if letter == 'X' else 'X' # switches player

            # if letter == 'X':
            #     letter = 'O'
            # else:
            #     letter = 'X'

        # tiny break to make things a little easier to read
        if print_game:
            time.sleep(0.8)

    if print_game:
        print('It\'s a tie!')

if __name__ == '__main__':
    """x_win = 0
    o_win = 0
    tie = 0
    for _ in range(10):
        x_player = RandomComputerPlayer('X')
        o_player = GeniusComputerPlayer('O')
        t = TicTacToe()
        result = play(t, x_player, o_player, print_game=True)
        if result == 'X':
            x_win += 1
        if result == 'O':
            o_win += 1
        else: 
            tie += 1
    print('after 100 iterations, {x_win} X win, {o_win} O wins and {tie} ties')"""
    x_player = HumanPlayer('X')
    o_player = GeniusComputerPlayer('O')
    t = TicTacToe()
    play(t, x_player, o_player, print_game=True)