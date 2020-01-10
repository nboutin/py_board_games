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
from connect_four.connect_four import (ConnectFour, Token)
from ai.minmax_alpha_beta import Minmax_AlphaBeta


class TestMinmaxAlphaBeta(unittest.TestCase):

    def test_perf(self):

        n = 10
        depth = 8
        p1 = Player("AI_1", Token.BLUE, True)
        duration = 0
        for i in range(n):
            minmax = Minmax_AlphaBeta(p1, depth, ConnectFour._MOVES)
            game = ConnectFour(p1=p1)

            start = time.time()
            minmax.compute(game)
            duration += time.time() - start

        self.assertAlmostEqual(duration / n, 1.0, delta=0.10)


if __name__ == '__main__':
    unittest.main()
