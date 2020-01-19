#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os
# sys.path.insert(0, os.path.join(sys.path[0], 'source'))
sys.path.insert(0, os.path.join(sys.path[0], '..', '..', 'source'))

# print(sys.path)

import cProfile
import pstats
from pstats import SortKey


from game_base.player import Player
from game_base.board import Token, Point
from game.connect_four import ConnectFour
from ai.minmax_alpha_beta import Minmax_AlphaBeta


def main():
    pr = cProfile.Profile()
    pr.enable()

    depth = 8
    p1 = Player("AI_1", Token.A, True)
    game = ConnectFour(p1=p1)
    minmax = Minmax_AlphaBeta(p1, depth)

    moves = [4,3,4,4,5,6]
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
    ps.print_callers()


if __name__ == "__main__":
    main()
