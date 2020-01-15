#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
import sys
import os
import time
sys.path.insert(0, os.path.join(sys.path[0], 'source'))
# sys.path.insert(0, os.path.join(sys.path[0], '..', '..', 'source'))


from game_base.board import (Point, Board)
from game_base.player import Player
from ai.minmax_alpha_beta import Minmax_AlphaBeta


class TestPerformance(unittest.TestCase):

    @unittest.skip("Performance")
    def test_connect_four(self):

        from game.connect_four import (ConnectFour, Token)

        n = 20
        depth = 8
        p1 = Player("AI_1", Token.A, True)
        duration = 0
        for i in range(n):
            minmax = Minmax_AlphaBeta(p1, depth)
            game = ConnectFour(p1=p1)

            start = time.time()
            minmax.compute(game)
            duration += time.time() - start

#         excepted = 1.027 # H
        excepted = 0.685  # W
        delta = excepted * 5 / 100
        print("Duration {}".format(duration / n))
        self.assertAlmostEqual(duration / n, excepted, delta=delta)

    @unittest.skip("Performance")
    def test_tictactoe(self):
        from game.tictactoe import TicTacToe, Token

        n = 10
        depth = 9
        p1 = Player("AI_1", Token.A, True)
        duration = 0
        for i in range(n):
            minmax = Minmax_AlphaBeta(p1, depth)
            game = TicTacToe(p1=p1)

            start = time.time()
            minmax.compute(game)
            duration += time.time() - start

#         excepted = 0.422 # H
        excepted = 0.219  # W
        delta = excepted * 5 / 100
        self.assertAlmostEqual(duration / n, excepted, delta=delta)

    @unittest.skip("Performance")
    def test_gomoku(self):
        from game.gomoku import (Gomoku, Token)

        n = 10
        depth = 6
        p1 = Player("AI_1", Token.A, True)
        duration = 0
        for i in range(n):
            game = Gomoku(column=7, row=7, p1=p1)
            minmax = Minmax_AlphaBeta(p1, depth)

            start = time.time()
            minmax.compute(game)
            duration += time.time() - start

#         excepted = 2.573 # H
        excepted = 1.336  # W
        delta = excepted * 5 / 100
        self.assertAlmostEqual(duration / n, excepted, delta=delta)


if __name__ == '__main__':
    unittest.main()
