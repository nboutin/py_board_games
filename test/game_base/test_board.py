#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
import sys
import os
sys.path.insert(0, os.path.join(sys.path[0], 'source'))

from game_base.board import (Board, Point)


class TestBoard(unittest.TestCase):

    def test_init_1_1(self):
        '''
        Test construction parameter and consistency with properties
        '''
        board = Board(1, 1)
        self.assertEqual(board._cell_free_count, 1)
        self.assertTrue(board.has_free_cell)
        self.assertEqual(board.cell_used_count, 0)

    def test_has_free_cell(self):
        board = Board(3, 3)

        for x in range(3):
            for y in range(3):
                self.assertTrue(board.has_free_cell())
                self.assertTrue(board.add_token(Point(x, y), "X"))

        self.assertFalse(board.has_free_cell())

    def test_cell_used_count(self):
        board = Board(3, 5)
        self.assertEqual(board.cell_used_count, 0)
        self.assertTrue(board.add_token(Point(0, 0), "X"))
        self.assertEqual(board.cell_used_count, 1)

    def test_add_token_on_used_cell(self):
        board = Board(2, 4)
        self.assertTrue(board.add_token(Point(0, 0), "X"))
        self.assertFalse(board.add_token(Point(0, 0), "X"))

    def test_boundaries(self):

        board = Board(3, 3)
        self.assertFalse(board.add_token(Point(-1, 0), "X"))
        self.assertFalse(board.add_token(Point(-2, -3), "X"))
        self.assertFalse(board.add_token(Point(0, -4), "X"))
        self.assertFalse(board.add_token(Point(3, 0), "X"))
        self.assertFalse(board.add_token(Point(3, 5), "X"))
        self.assertFalse(board.add_token(Point(0, 5), "X"))

    def test_undo(self):
        board = Board(4, 2)
        token = "X"
        self.assertTrue(board.add_token(Point(0, 0), token))
        self.assertTrue(board.add_token(Point(1, 0), token))

        self.assertEqual(board.cell_used_count, 2)
#         self.assertEqual(board._cell_free_column_count[0], Board._ROW - 1)
#         self.assertEqual(board._cell_free_column_count[1], Board._ROW - 1)
#         self.assertEqual(board.grid[5][0], token)
#         self.assertEqual(board.grid[5][1], token)

        board.undo(Point(1, 0))
        self.assertEqual(board.cell_used_count, 1)
#         self.assertEqual(board._cell_free_column_count[1], Board._ROW)

        self.assertEqual(board.grid[0][0], token)
        self.assertEqual(board.grid[0][1], None)


if __name__ == '__main__':
    unittest.main()
