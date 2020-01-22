#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os
sys.path.insert(0, os.path.join(sys.path[0], 'source'))
# sys.path.insert(0, os.path.join(sys.path[0], '..', '..', 'source'))

# print(sys.path)

import cProfile
import pstats
from pstats import SortKey


from game_base.player import Player
from game_base.board import Token, Point
from game.gomoku import Gomoku
from ai.minmax_alpha_beta import Minmax_AlphaBeta


def main():
    pr = cProfile.Profile()
    pr.enable()

    depth = 4
    p1 = Player("AI_1", Token.A, True)
    game = Gomoku(p1=p1, size=9)
    minmax = Minmax_AlphaBeta(p1, depth)

    moves = [Point(4, 4), Point(3, 3), Point(4, 3),
             Point(3, 4), Point(3, 2), Point(4, 5)]
    for m in moves:
        game.play(m)

    minmax.compute(game)

    pr.disable()

    # Construct stats
    ps = pstats.Stats(pr)
    ps.strip_dirs()
#     ps.sort_stats(SortKey.CUMULATIVE)
    ps.sort_stats('tottime')
    ps.print_stats()


if __name__ == "__main__":
    main()
