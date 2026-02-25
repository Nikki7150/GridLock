import math
import random

class Player:
    def __init__(self, letter):
        # letter is x or o
        self.letter = letter

    # we want all players to ger their next move
    def get_move(self, game):
        pass


class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        # get a random valid spot for our next move
        square = random.choice(game.available_moves())
        return square

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + '\'s turn. Input move (0-8): ')
            # we're going to check that this is a correct value by trying to cast
            # it into an integer, an dif its not, then we say its invalid
            # if that spot is not available on the board, we also say its invalid
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True # if these are successful, then yay!
            except ValueError:
                print('Invalid square. Try again.')

        return val
    

# unbeatable algorithm
class GeniusComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        if len(game.available_moves()) == 0:
            square = random.choice(game.available_moves()) # randomly choose one
        else: 
            # get the square based on the minmax algorithm
            square = self.minimax(game, self.letter)['position']
        return square
    
    def minimax (self, state, player): # state = screenshot of game
        max_player = self.letter # yourself
        other_player = 'O' if player == 'X' else 'X' 

        # check if previous move is a winner
        # this is base case - at end, where are we at
        # was there a winner in the states passed in
        if state.current_winner == other_player:
            return {'position': None, 
                    'score': 1 * (state.num_empty_squares() + 1) if other_player == max_player else -1 * (
                        state.num_empty_squares() + 1)
                    }
        
        elif not state.num_empty_squares(): # no empty squares
            return {'position': None, 'score': 0}
        
        if player == max_player:# save best position and best score
            best = {'position': None, 'score': -math.inf} # each score should maximize
        else: 
            best = {'position': None, 'score': math.inf} # each score should minimize

        for possible_move in state.available_moves():
            # 1: make a move, try that spot
            state.make_move(possible_move, player)
            # 2: recurse using minimac to stimulate a game after making the move
            sim_score = self.minimax(state, other_player) # alrternate player
            # 3: undo the move
            state.board[possible_move] = ' '
            state.current_winner = None
            sim_score['position'] = possible_move # otherwise this will get messed up from recursion

            # 4: update the dictionaries if necessary
            if player == max_player: # maximize max_player
                if sim_score['score'] > best['score']:
                    best = sim_score # replace best
            else: # minimize other player
                if sim_score['score'] < best['score']:
                    best = sim_score # replace best

        return best