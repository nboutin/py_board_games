#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import version
from game_base.board import Point
from game_base.player import Player
from gomoku.gomoku import (Gomoku, Token)
from gomoku.ascii_view import ASCII_View
from ai.minmax_alpha_beta import Minmax_AlphaBeta


def main():

    mode = input("Select mode (0:H_H, 1:AI_H, 2:H_AI, 3:AI_AI):")
    p1, p2 = select_mode(int(mode))

    level = input("Choose level (4):")
    level = 4 if not level else int(level)

    game = Gomoku(p1=p1, p2=p2)

    if p1.is_ai:
        minmax1 = Minmax_AlphaBeta(p1, level, game._moves)
    if p2.is_ai:
        minmax2 = Minmax_AlphaBeta(p2, level, game._moves)

    view = ASCII_View(game.grid)
    view.welcome("Gomoku", version.VERSION)

    while game.is_over == False:
        view.current_player = game.current_player
        view.display()

        if game.current_player.is_ai:
            if game.current_player == p1:
                mm = minmax1
            elif game.current_player == p2:
                mm = minmax2

            p = mm.compute(game)
            view.add_message("Move: {} ({}s)".format(p, mm.computation_time))
        else:
            x, y = view.ask_input()
            p = Point(x, y)

        if not game.play(p):
            view.message("Input is invalid")


    view.set_history(game.history)
    if game.winner is None:
        view.add_message("Game is finished. Draw")
    else:
        view.add_message(
            "Game is finished. Winner is {}".format(game.winner.name))
    view.display()


def select_mode(mode):

    p1, p2 = None, None

    if mode == 0:
        p1 = Player("Player_1", Token.CROSS)
        p2 = Player("Player_2", Token.CIRCLE)
    elif mode == 1:
        p1 = Player("AI_1", Token.CROSS, True)
        p2 = Player("Player_2", Token.CIRCLE)
    elif mode == 2:
        p1 = Player("Player_1", Token.CROSS)
        p2 = Player("AI_2", Token.CIRCLE, True)
    elif mode == 3:
        p1 = Player("AI_1", Token.CROSS, True)
        p2 = Player("AI_2", Token.CIRCLE, True)

    return p1, p2


if __name__ == "__main__":
    main()