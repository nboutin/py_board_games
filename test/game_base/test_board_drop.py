#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
import sys
import os
sys.path.insert(0, os.path.join(sys.path[0], 'source'))

from game_base.board_drop import BoardDrop


class TestBoard(unittest.TestCase):

    def test_boundaries(self):

        col = 6
        row = 7
        token = "x"

        board = BoardDrop(col, row)
        self.assertFalse(board.drop_token(-1, token))
        self.assertFalse(board.drop_token(col, token))
        self.assertFalse(board.drop_token(col + 1, token))

    def test_drop(self):
        board = BoardDrop(2, 3)
        token = "X"

        self.assertTrue(board.drop_token(0, token))
        self.assertTrue(board.has_free_cell)
        self.assertEqual(board.cell_used_count, 1)
        self.assertEqual(board._cell_free_column_count[0], 3 - 1)
        self.assertEqual(board.grid[2][0], token)

    def test_undo(self):
        board = BoardDrop(2, 3)
        token = "X"

        self.assertTrue(board.drop_token(0, token))
        self.assertTrue(board.drop_token(0, token))
        self.assertEqual(board.grid[1][0], token)
        self.assertTrue(board.undo(0))
        self.assertEqual(board.grid[1][0], None)


if __name__ == '__main__':
    unittest.main()
