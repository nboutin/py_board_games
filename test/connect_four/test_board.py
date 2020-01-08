#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
import sys
import os
sys.path.insert(0, os.path.join(sys.path[0], 'source'))

from connect_four.board import (Board, Point, Token)


class TestBoard(unittest.TestCase):

    def test_has_free_cell(self):
        '''
        PLay token until the board is full'''
        board = Board()

        for x in range(Board._COLUMN):
            for y in range(Board._ROW):
                self.assertTrue(board.has_free_cell())
                self.assertTrue(board.play(x, Token.BLUE))

        self.assertFalse(board.has_free_cell())

    def test_played_cell_count(self):
        '''
        Check that token count increments when token is played'''
        board = Board()
        self.assertEqual(board.cell_played_count, 0)

        self.assertTrue(board.play(0, Token.BLUE))
        self.assertEqual(board.cell_played_count, 1)

        self.assertTrue(board.play(1, Token.BLUE))
        self.assertEqual(board.cell_played_count, 2)

    def test_play_busy_row(self):
        board = Board()
        x_min = 0
        x_max = Board._COLUMN - 1

        for i in range(Board._ROW):
            self.assertTrue(board.play(x_min, Token.BLUE))
            self.assertTrue(board.play(x_max, Token.BLUE))

        self.assertFalse(board.play(x_min, Token.BLUE))
        self.assertFalse(board.play(x_max, Token.BLUE))

    def test_boundaries(self):

        board = Board()
        self.assertFalse(board.play(-1, Token.BLUE))
        self.assertFalse(board.play(Board._COLUMN, Token.BLUE))
        self.assertFalse(board.play(Board._COLUMN + 1, Token.BLUE))

    def test_undo(self):
        board = Board()
        self.assertTrue(board.play(0, Token.BLUE))
        self.assertTrue(board.play(1, Token.BLUE))

        self.assertEqual(board.cell_played_count, 2)
        self.assertEqual(board._cell_free_column_count[0], Board._ROW - 1)
        self.assertEqual(board._cell_free_column_count[1], Board._ROW - 1)

        board.undo(1)
        self.assertEqual(board.cell_played_count, 1)
        self.assertEqual(board._cell_free_column_count[1], Board._ROW)
        
    def test_check_line_horizontal(self):
        board = Board()
        
        x_max = Board._COLUMN - 1
        y_max = Board._ROW - 1
        
        self.assertFalse(board.check_line_horizontal(0, x_max, y_max, [Token.BLUE]))
        self.assertTrue(board.play(0, Token.BLUE))
        self.assertTrue(board.check_line_horizontal(0, x_max, y_max, [Token.BLUE]))
        
        self.assertTrue(board.play(1, Token.BLUE))
        self.assertTrue(board.check_line_horizontal(0, x_max, y_max, [Token.BLUE, Token.BLUE]))

        self.assertTrue(board.play(2, Token.BLUE))
        self.assertTrue(board.check_line_horizontal(0, x_max, y_max, [Token.BLUE, Token.BLUE, Token.BLUE]))

if __name__ == '__main__':
    unittest.main()
