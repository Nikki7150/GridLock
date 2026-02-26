from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from game import TicTacToe

app = Flask(__name__)
CORS(app)

game = TicTacToe()
game_mode = "human-player" # default mode
current_letter = "X"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/move", methods=['POST'])
def move():
    global current_letter

    data = request.get_json()
    square = data.get("square")

    if game.make_move(square, current_letter):

        if game_mode == "multiplayer":
            # just switch turns
            current_letter = "O" if current_letter == "X" else "X"

        else:
            # AI modes
            if game.empty_squares() and not game.current_winner:
                from player import GeniusComputerPlayer, RandomComputerPlayer

                if game_mode == "genius_computer":
                    op = GeniusComputerPlayer("O")
                else:
                    op = RandomComputerPlayer("O")

                op_square = op.get_move(game)
                game.make_move(op_square, "O")

    return jsonify({
        "board": game.board,
        "winner": game.current_winner,
        "tie": not game.empty_squares() and not game.current_winner,
        "winning_cells": game.winning_cells
    })

@app.route("/reset", methods=["POST"])
def reset():
    global game, current_letter
    game = TicTacToe()
    current_letter="X"
    return jsonify ({"message": "Game Reset"})

@app.route("/set_mode", methods=["POST"])
def set_mode():
    global game_mode, game

    data = request.get_json()
    mode = data.get("mode")

    game_mode = mode
    game = TicTacToe() # RESET BOARD WHEN CHANGE

    return jsonify({"message": "Mode set"})

if __name__ == "__main__":
    app.run()