#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
import sys
import os
sys.path.insert(0, os.path.join(sys.path[0], 'source'))

from tictactoe.tictactoe import TicTacToe
from tictactoe.board import (Token, Point)


class TestTicTacToe(unittest.TestCase):

    def test_init(self):
        game = TicTacToe()
        self.assertFalse(game.is_over)
        self.assertEqual(game.winner, None)
        self.assertEqual(len(game.history), 0)
        self.assertEqual(game._current_player, game._p1)

    def test_next_player(self):
        game = TicTacToe()

        self.assertEqual(game._current_player, game._p1)
        self.assertTrue(game.play(Point(0, 0)))
        self.assertEqual(game._current_player, game._p2)
        self.assertTrue(game.play(Point(1, 0)))
        self.assertEqual(game._current_player, game._p1)

        # Cell not free, do not change current player
        self.assertFalse(game.play(Point(1, 0)))
        self.assertEqual(game._current_player, game._p1)

    def test_win_horizontal_player1(self):
        game = TicTacToe()

        self.assertTrue(game.play(Point(0, 0)))
        self.assertTrue(game.play(Point(0, 1)))
        self.assertTrue(game.play(Point(1, 0)))
        self.assertTrue(game.play(Point(1, 1)))
        self.assertTrue(game.play(Point(2, 0)))

        self.assertTrue(game.is_over)
        self.assertEqual(game.winner, game._p1)

    def test_win_horizontal_player2(self):
        game = TicTacToe()

        self.assertTrue(game.play(Point(0, 0)))
        self.assertTrue(game.play(Point(0, 1)))
        self.assertTrue(game.play(Point(1, 0)))
        self.assertTrue(game.play(Point(1, 1)))
        self.assertTrue(game.play(Point(0, 2)))
        self.assertTrue(game.play(Point(2, 1)))

        self.assertTrue(game.is_over)
        self.assertEqual(game.winner, game._p2)

    def test_draw(self):
        game = TicTacToe()
        self.assertTrue(game.play(Point(0, 0)))
        self.assertTrue(game.play(Point(1, 0)))
        self.assertTrue(game.play(Point(2, 0)))
        self.assertTrue(game.play(Point(0, 1)))
        self.assertTrue(game.play(Point(1, 1)))
        self.assertTrue(game.play(Point(2, 2)))
        self.assertTrue(game.play(Point(1, 2)))
        self.assertTrue(game.play(Point(0, 2)))
        self.assertTrue(game.play(Point(2, 1)))

        self.assertTrue(game.is_over)
        self.assertEqual(game.winner, None)

    def test_win_vertical_player1(self):
        game = TicTacToe()
        self.assertTrue(game.play(Point(0, 0)))
        self.assertTrue(game.play(Point(1, 0)))
        self.assertTrue(game.play(Point(0, 1)))
        self.assertTrue(game.play(Point(1, 1)))
        self.assertTrue(game.play(Point(0, 2)))

        self.assertTrue(game.is_over)
        self.assertEqual(game.winner, game._p1)

    def test_win_vertical_player2(self):
        game = TicTacToe()
        self.assertTrue(game.play(Point(0, 0)))
        self.assertTrue(game.play(Point(2, 0)))
        self.assertTrue(game.play(Point(0, 1)))
        self.assertTrue(game.play(Point(2, 1)))
        self.assertTrue(game.play(Point(1, 0)))
        self.assertTrue(game.play(Point(2, 2)))

        self.assertTrue(game.is_over)
        self.assertEqual(game.winner, game._p2)

    def test_win_diag_player1(self):
        game = TicTacToe()
        self.assertTrue(game.play(Point(0, 0)))
        self.assertTrue(game.play(Point(1, 0)))
        self.assertTrue(game.play(Point(1, 1)))
        self.assertTrue(game.play(Point(2, 0)))
        self.assertTrue(game.play(Point(2, 2)))

        self.assertTrue(game.is_over)
        self.assertEqual(game.winner, game._p1)

    def test_win_diag_player2(self):
        game = TicTacToe()
        self.assertTrue(game.play(Point(0, 0)))
        self.assertTrue(game.play(Point(0, 2)))
        self.assertTrue(game.play(Point(1, 0)))
        self.assertTrue(game.play(Point(1, 1)))
        self.assertTrue(game.play(Point(0, 1)))
        self.assertTrue(game.play(Point(2, 0)))

        self.assertTrue(game.is_over)
        self.assertEqual(game.winner, game._p2)


if __name__ == '__main__':
    unittest.main()
