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
from ai.minmax_ab import Minmax_AB

# Enable
all = False
tictactoe = False
connect_four = True
gomoku = False

# Home
expected = {'tictactoe': 0.422, 'connect_four': 110000, 'gomoku': 1.701}
# Work
# expected = {'tictactoe': 0.52, 'connect_four': 174777, 'gomoku': 0.77}


class TestPerformance(unittest.TestCase):
    '''
    @todo add test for tictactoe play and compute_ending
    '''

    @unittest.skipIf(not(all or tictactoe), "Performance")
    def test_tictactoe(self):
        from game.tictactoe import TicTacToe

        n = 10
        depth = 9
        duration = 0
        p1 = Player("AI_1", Token.A, True)
        for i in range(n):
            minmax = Minmax_AB(p1, depth)
            game = TicTacToe(p1=p1)

            start = time.time()
            minmax.compute(game)
            duration += time.time() - start

        print("Duration {}".format(duration / n))

        r = expected['tictactoe']
        delta = r * 3 / 100
        self.assertAlmostEqual(duration / n, r, delta=delta)

    @unittest.skipIf(not(all or connect_four), "Performance")
    def test_connect_four(self):

        from game.connect_four import ConnectFour

        n = 10
        depth = 11
        p1 = Player("AI_1", Token.A, True)
        duration = 0
        move_count = 0
        for i in range(n):
            minmax = Minmax_AB(p1, depth)
            game = ConnectFour(p1=p1)
            for m in [0, 2, 0, 3]:
                game.play(m)

            start = time.time()
            minmax.compute(game)
            duration += time.time() - start
            move_count += minmax._move_count

        r = move_count / duration
        e = expected['connect_four']
        d = r * 3 / 100

        print("Move/second: {} (+/- {})".format(int(move_count / duration), int(d)))
        self.assertAlmostEqual(r, e, delta=d)

    @unittest.skipIf(not(all or gomoku), "Performance")
    def test_gomoku(self):
        from game.gomoku import Gomoku

        n = 15
        depth = 4
        p1 = Player("AI_1", Token.A, True)
        duration = 0
        for i in range(n):
            game = Gomoku(p1=p1, size=9)
            minmax = Minmax_AB(p1, depth)

            moves = [Point(4, 4), Point(3, 3), Point(4, 3),
                     Point(3, 4), Point(3, 2), Point(4, 5)]
            for m in moves:
                game.play(m)

            start = time.time()
            minmax.compute(game)
            duration += time.time() - start

        print('Duration {}'.format(duration / n))
        r = expected['gomoku']
        delta = r * 3 / 100
        self.assertAlmostEqual(duration / n, r, delta=delta)


if __name__ == '__main__':
    unittest.main()
