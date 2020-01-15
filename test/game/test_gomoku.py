#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
import sys
import os
sys.path.insert(0, os.path.join(sys.path[0], 'source'))

from game.gomoku import (Gomoku, Token)
from game_base.board import (Point)


class TestGomoku(unittest.TestCase):

    def test_init(self):
        game = Gomoku()
        self.assertEqual(game._current_player, game._p1)
        self.assertEqual(game.winner, None)
        self.assertFalse(game.is_over)
        self.assertEqual(len(game.history), 0)

    def test_next_player(self):
        game = Gomoku()

        self.assertEqual(game._current_player, game._p1)
        self.assertTrue(game.play(Point(0, 0)))
        self.assertEqual(game._current_player, game._p2)
        self.assertTrue(game.play(Point(1, 0)))
        self.assertEqual(game._current_player, game._p1)

        # Cell not free, do not change current player
        self.assertFalse(game.play(Point(1, 0)))
        self.assertEqual(game._current_player, game._p1)

    def test_win_horizontal_player1(self):

        game = Gomoku()

        self.assertTrue(game.play(Point(0, 0)))
        self.assertTrue(game.play(Point(0, 1)))
        self.assertTrue(game.play(Point(1, 0)))
        self.assertTrue(game.play(Point(1, 1)))
        self.assertTrue(game.play(Point(2, 0)))
        self.assertTrue(game.play(Point(2, 1)))
        self.assertTrue(game.play(Point(3, 0)))
        self.assertTrue(game.play(Point(3, 1)))
        self.assertTrue(game.play(Point(4, 0)))
        # Cannot play anymore, game is over
        self.assertFalse(game.play(Point(4, 1)))

        self.assertTrue(game.is_over)
        self.assertEqual(game.winner, game._p1)

    def test_win_horizontal_all(self):

        for len in [7, 9, 11]:
            for x in range(len - Gomoku._LINE_WIN_SIZE + 1):
                for y in range(len - 1):
                    game = Gomoku(column=len, row=len)

                    self.assertTrue(game.play(Point(x + 0, y + 0)))
                    self.assertTrue(game.play(Point(x + 0, y + 1)))
                    self.assertTrue(game.play(Point(x + 1, y + 0)))
                    self.assertTrue(game.play(Point(x + 1, y + 1)))
                    self.assertTrue(game.play(Point(x + 2, y + 0)))
                    self.assertTrue(game.play(Point(x + 2, y + 1)))
                    self.assertTrue(game.play(Point(x + 3, y + 0)))
                    self.assertTrue(game.play(Point(x + 3, y + 1)))
                    self.assertTrue(game.play(Point(x + 4, y + 0)))
                    # Cannot play anymore, game is over
                    self.assertFalse(game.play(Point(4, 1)))

                    self.assertTrue(game.is_over)
                    self.assertEqual(game.winner, game._p1)

    def test_win_horizontal_player2(self):
        game = Gomoku()

        self.assertTrue(game.play(Point(0, 0)))
        self.assertTrue(game.play(Point(0, 1)))
        self.assertTrue(game.play(Point(1, 0)))
        self.assertTrue(game.play(Point(1, 1)))
        self.assertTrue(game.play(Point(2, 0)))
        self.assertTrue(game.play(Point(2, 1)))
        self.assertTrue(game.play(Point(3, 0)))
        self.assertTrue(game.play(Point(3, 1)))
        self.assertTrue(game.play(Point(0, 2)))
        self.assertTrue(game.play(Point(4, 1)))

        self.assertTrue(game.is_over)
        self.assertEqual(game.winner, game._p2)

    def test_draw(self):
        history = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6),
                   (1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6),
                   (2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (3, 2), (4, 1),
                   (3, 3), (2, 5), (2, 6), (3, 0), (3, 1), (3, 4), (3, 5),
                   (3, 6), (4, 0), (4, 2), (4, 3), (5, 4), (4, 4), (5, 3),
                   (4, 5), (4, 6), (5, 0), (5, 1), (5, 2), (5, 5), (5, 6),
                   (6, 0), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 6)]
        game = Gomoku(column=7, row=7)

        for x, y in history:
            self.assertTrue(game.play(Point(x, y)))

        self.assertTrue(game.is_over)
        self.assertEqual(game.winner, None)

    def test_win_vertical_player1(self):
        game = Gomoku()
        self.assertTrue(game.play(Point(0, 0)))
        self.assertTrue(game.play(Point(1, 0)))
        self.assertTrue(game.play(Point(0, 1)))
        self.assertTrue(game.play(Point(1, 1)))
        self.assertTrue(game.play(Point(0, 2)))
        self.assertTrue(game.play(Point(1, 2)))
        self.assertTrue(game.play(Point(0, 3)))
        self.assertTrue(game.play(Point(1, 3)))
        self.assertTrue(game.play(Point(0, 4)))

        self.assertTrue(game.is_over)
        self.assertEqual(game.winner, game._p1)

    def test_win_vertical_all(self):
        for len in [7, 9, 11]:
            for x in range(len - 1):
                for y in range(len - Gomoku._LINE_WIN_SIZE + 1):
                    game = Gomoku(column=len, row=len)
                    self.assertTrue(game.play(Point(x + 0, y + 0)))
                    self.assertTrue(game.play(Point(x + 1, y + 0)))
                    self.assertTrue(game.play(Point(x + 0, y + 1)))
                    self.assertTrue(game.play(Point(x + 1, y + 1)))
                    self.assertTrue(game.play(Point(x + 0, y + 2)))
                    self.assertTrue(game.play(Point(x + 1, y + 2)))
                    self.assertTrue(game.play(Point(x + 0, y + 3)))
                    self.assertTrue(game.play(Point(x + 1, y + 3)))
                    self.assertTrue(game.play(Point(x + 0, y + 4)))

                    self.assertTrue(game.is_over)
                    self.assertEqual(game.winner, game._p1)

    def test_win_vertical_player2(self):
        game = Gomoku()
        self.assertTrue(game.play(Point(0, 0)))
        self.assertTrue(game.play(Point(1, 0)))
        self.assertTrue(game.play(Point(0, 1)))
        self.assertTrue(game.play(Point(1, 1)))
        self.assertTrue(game.play(Point(0, 2)))
        self.assertTrue(game.play(Point(1, 2)))
        self.assertTrue(game.play(Point(0, 3)))
        self.assertTrue(game.play(Point(1, 3)))
        self.assertTrue(game.play(Point(2, 4)))
        self.assertTrue(game.play(Point(1, 4)))

        self.assertTrue(game.is_over)
        self.assertEqual(game.winner, game._p2)

    def test_win_diag_down_player1(self):
        game = Gomoku()
        self.assertTrue(game.play(Point(0, 0)))
        self.assertTrue(game.play(Point(1, 0)))
        self.assertTrue(game.play(Point(1, 1)))
        self.assertTrue(game.play(Point(2, 0)))
        self.assertTrue(game.play(Point(2, 2)))
        self.assertTrue(game.play(Point(3, 0)))
        self.assertTrue(game.play(Point(3, 3)))
        self.assertTrue(game.play(Point(4, 0)))
        self.assertTrue(game.play(Point(4, 4)))

        self.assertTrue(game.is_over)
        self.assertEqual(game.winner, game._p1)

    def test_win_diag_down_all(self):

        for len in [7, 9, 11]:
            for x in range(len - 5 + 1):
                for y in range(len - 5 + 1):
                    game = Gomoku(column=len, row=len)
                    self.assertTrue(game.play(Point(x + 0, y + 0)))
                    self.assertTrue(game.play(Point(x + 1, y + 0)))
                    self.assertTrue(game.play(Point(x + 1, y + 1)))
                    self.assertTrue(game.play(Point(x + 2, y + 0)))
                    self.assertTrue(game.play(Point(x + 2, y + 2)))
                    self.assertTrue(game.play(Point(x + 3, y + 0)))
                    self.assertTrue(game.play(Point(x + 3, y + 3)))
                    self.assertTrue(game.play(Point(x + 4, y + 0)))
                    self.assertTrue(game.play(Point(x + 4, y + 4)))

                    self.assertTrue(game.is_over)
                    self.assertEqual(game.winner, game._p1)

    def test_win_diag_up_player1(self):
        game = Gomoku()
        self.assertTrue(game.play(Point(4, 0)))
        self.assertTrue(game.play(Point(0, 0)))
        self.assertTrue(game.play(Point(3, 1)))
        self.assertTrue(game.play(Point(1, 0)))
        self.assertTrue(game.play(Point(2, 2)))
        self.assertTrue(game.play(Point(2, 0)))
        self.assertTrue(game.play(Point(1, 3)))
        self.assertTrue(game.play(Point(0, 1)))
        self.assertTrue(game.play(Point(0, 4)))

        self.assertTrue(game.is_over)
        self.assertEqual(game.winner, game._p1)

    def test_win_diag_up_all(self):
        for len in [7, 9, 11]:
            for x in range(len - 5 + 1):
                for y in range(len - 5 + 1):
                    game = Gomoku(column=len, row=len)
                    self.assertTrue(game.play(Point(x + 4, y + 0)))
                    self.assertTrue(game.play(Point(x + 0, y + 0)))
                    self.assertTrue(game.play(Point(x + 3, y + 1)))
                    self.assertTrue(game.play(Point(x + 1, y + 0)))
                    self.assertTrue(game.play(Point(x + 2, y + 2)))
                    self.assertTrue(game.play(Point(x + 2, y + 0)))
                    self.assertTrue(game.play(Point(x + 1, y + 3)))
                    self.assertTrue(game.play(Point(x + 0, y + 1)))
                    self.assertTrue(game.play(Point(x + 0, y + 4)))

                    self.assertTrue(game.is_over)
                    self.assertEqual(game.winner, game._p1)


if __name__ == '__main__':
    unittest.main()
