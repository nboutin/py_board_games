#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tictactoe.tictactoe import TicTacToe
from tictactoe.board import Point
from view.ascii_view import ASCII_View

__VERSION = "1.0.0"

def main():

    game = TicTacToe()
    view = ASCII_View(game.grid)
    view.welcome("TicTacToe", __VERSION)

    while game.is_over == False:
        view.current_player = game.current_player
        view.display()
        x, y = view.ask_input()

        if not game.play(Point(x, y)):
            view.message("Input is invalid")
    
    if game.winner is None:
        view.message("Game is finished. Draw")
    else:
        view.message("Game is finished. Winner is {}".format(game.winner.name))
    view.display()

if __name__ == "__main__":
    main()
