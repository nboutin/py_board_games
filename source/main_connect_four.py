#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from connect_four.connect_four import ConnectFour
from connect_four.board import (Point, Token)
from connect_four.player import Player
from connect_four.ascii_view import ASCII_View
from ai.minmax import Minmax
from ai.minmax_alpha_beta import Minmax_AlphaBeta

__VERSION = "1.2.0-dev"

__MOVES = [0, 1, 2, 3, 4, 5, 6]


def main():

    mode = input("Select mode (0:H_H, 1:AI_H, 2:H_AI, 3:AI_AI):")
    p1, p2 = select_mode(int(mode))

    game = ConnectFour(p1=p1, p2=p2)

    depth = 9
    if p1.is_ai:
        minmax1 = Minmax_AlphaBeta(p1, depth, __MOVES)
    if p2.is_ai:
        minmax2 = Minmax_AlphaBeta(p2, depth, __MOVES)

    view = ASCII_View(game.grid)
    view.welcome("Connect Four", __VERSION)

    while game.is_over == False:
        view.current_player = game.current_player
        view.display()

        if game.current_player.is_ai:
            if game.current_player == p1:
                mm = minmax1
            elif game.current_player == p2:
                mm = minmax2

            move = mm.compute(game)
            view.message("Move: {} ({}s)".format(move, mm.computation_time))
        else:
            move = view.ask_input()

        if not game.play(move):
            view.message("Input is invalid")

    if game.winner is None:
        view.message("Game is finished. Draw")
    else:
        view.message("Game is finished. Winner is {}".format(game.winner.name))
    view.display()


def select_mode(mode):

    p1, p2 = None, None

    if mode == 0:
        p1 = Player("Player_1", Token.BLUE)
        p2 = Player("Player_2", Token.RED)
    elif mode == 1:
        p1 = Player("AI_1", Token.BLUE, True)
        p2 = Player("Player_2", Token.RED)
    elif mode == 2:
        p1 = Player("Player_1", Token.BLUE)
        p2 = Player("AI_2", Token.RED, True)
    elif mode == 3:
        p1 = Player("AI_1", Token.BLUE, True)
        p2 = Player("AI_2", Token.RED, True)

    return p1, p2


if __name__ == "__main__":
    main()
