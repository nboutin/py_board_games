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

        from connect_four.connect_four import (ConnectFour, Token)

        n = 10
        depth = 8
        p1 = Player("AI_1", Token.BLUE, True)
        duration = 0
        for i in range(n):
            minmax = Minmax_AlphaBeta(p1, depth, ConnectFour.MOVES)
            game = ConnectFour(p1=p1)

            start = time.time()
            minmax.compute(game)
            duration += time.time() - start

        excepted = 0.777
        delta = excepted / 10  # 10%
        self.assertAlmostEqual(duration / n, excepted, delta=delta)

    @unittest.skip("Performance")
    def test_gomoku(self):
        from gomoku.gomoku import (Gomoku, Token)

        n = 10
        depth = 6
        p1 = Player("AI_1", Token.CROSS, True)
        duration = 0
        for i in range(n):
            game = Gomoku(p1=p1)
            minmax = Minmax_AlphaBeta(p1, depth, game._moves)

            start = time.time()
            minmax.compute(game)
            duration += time.time() - start

        excepted = 1.336
        delta = excepted / 5  # 5%
        self.assertAlmostEqual(duration / n, excepted, delta=delta)


if __name__ == '__main__':
    unittest.main()
