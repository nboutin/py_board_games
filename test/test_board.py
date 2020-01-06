#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
import sys
import os
sys.path.insert(0, os.path.join(sys.path[0], 'source'))

from tictactoe.board import (Board, Point, Token)


class TestBoard(unittest.TestCase):

    def test_has_free_cell(self):
        board = Board()

        for x in range(3):
            for y in range(3):
                self.assertTrue(board.has_free_cell())
                self.assertTrue(board.play(Point(x, y), Token.CROSS))

        self.assertFalse(board.has_free_cell())
        
    def test_played_cell_count(self):
        board = Board()
        self.assertEqual(board.played_cell_count, 0)
        self.assertTrue(board.play(Point(0, 0), Token.CROSS))
        self.assertEqual(board.played_cell_count, 1)

    def test_play_busy_cell(self):
        board = Board()
        self.assertTrue(board.play(Point(0, 0), Token.CROSS))
        self.assertFalse(board.play(Point(0, 0), Token.CROSS))

    def test_boundaries(self):

        board = Board()
        self.assertFalse(board.play(Point(-1, 0), Token.CROSS))
        self.assertFalse(board.play(Point(-2, -3), Token.CROSS))
        self.assertFalse(board.play(Point(0, -4), Token.CROSS))
        self.assertFalse(board.play(Point(3, 0), Token.CROSS))
        self.assertFalse(board.play(Point(3, 5), Token.CROSS))
        self.assertFalse(board.play(Point(0, 5), Token.CROSS))


if __name__ == '__main__':
    unittest.main()
