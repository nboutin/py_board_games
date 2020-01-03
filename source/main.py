#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tictactoe.tictactoe import TicTacToe
from tictactoe.board import Point
from view.ascii_view import ASCII_View


def main():

    game = TicTacToe()
    view = ASCII_View(game.grid)

    while game.is_over == False:
        view.display()
        x, y = view.ask_input()

        if not game.play(Point(x, y)):
            view.message("Input is invalid")
    
    view.message("Game is finished. Winner is {}".format(game.winner.name))
    view.display()

if __name__ == "__main__":
    main()
