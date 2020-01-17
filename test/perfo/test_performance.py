#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
import sys
import os
import time
sys.path.insert(0, os.path.join(sys.path[0], 'source'))
# sys.path.insert(0, os.path.join(sys.path[0], '..', '..', 'source'))


from game_base.board import (Point, Board, Token)
from game_base.player import Player
from ai.minmax_alpha_beta import Minmax_AlphaBeta


class TestPerformance(unittest.TestCase):
    '''
    @todo add test for tictactoe play and compute_ending
    '''

#     @unittest.skip("Performance")
    def test_tictactoe(self):
        from game.tictactoe import TicTacToe

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

        excepted = 0.422 # H
#         excepted = 0.150  # W
        print("Duration {}".format(duration / n))
        delta = excepted * 3 / 100
        self.assertAlmostEqual(duration / n, excepted, delta=delta)

    @unittest.skip("Performance")
    def test_connect_four(self):

        from game.connect_four import ConnectFour

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
    def test_gomoku(self):
        from game.gomoku import Gomoku

        n = 7
        depth = 4
        p1 = Player("AI_1", Token.A, True)
        duration = 0
        for i in range(n):
            game = Gomoku(p1=p1, size=9)
            minmax = Minmax_AlphaBeta(p1, depth)

            moves = [Point(4, 4), Point(3, 3), Point(4, 3),
                     Point(3, 4), Point(3, 2), Point(4, 5)]
            for m in moves:
                game.play(m)

            start = time.time()
            minmax.compute(game)
            duration += time.time() - start

#         excepted = 2.573 # H
        excepted = 1.630  # W
        delta = excepted * 3 / 100
        print('Duration {}, delta {}'.format(duration / n, delta))
        self.assertAlmostEqual(duration / n, excepted, delta=delta)


if __name__ == '__main__':
    unittest.main()
