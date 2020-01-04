#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tictactoe.tictactoe import TicTacToe
from tictactoe.board import (Point, Token)
from tictactoe.player import Player
from view.ascii_view import ASCII_View
from ai.minmax import Minmax

__VERSION = "1.1.0-dev"

def main():

    ai_player = Player("AI_1", Token.CROSS, True)
    game = TicTacToe(p1 = ai_player)
    minmax = Minmax(ai_player, 7)
    
    view = ASCII_View(game.grid)
    view.welcome("TicTacToe", __VERSION)

    while game.is_over == False:
        view.current_player = game.current_player
        view.display()

        if game.current_player.is_ai:
            p = minmax.compute(game)
        else:
            x,y = view.ask_input()
            p = Point(x,y)

        if not game.play(p):
            view.message("Input is invalid")
    
    if game.winner is None:
        view.message("Game is finished. Draw")
    else:
        view.message("Game is finished. Winner is {}".format(game.winner.name))
    view.display()

if __name__ == "__main__":
    main()
