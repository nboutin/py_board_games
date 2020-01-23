#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
import copy
import sys
import os
sys.path.insert(0, os.path.join(sys.path[0], 'source'))

from game_base.board import (Board, Point)


class TestBoard(unittest.TestCase):

    def test_deepcopy(self):
        w, h = 5, 3
        b = Board(w, h)

        cb = copy.deepcopy(b)

        self.assertFalse(b is cb)
        self.assertFalse(b._grid is cb._grid)
        self.assertFalse(b._moves is cb._moves)

    def test_x_y_order(self):
        w, h = 5, 3
        board = Board(w, h)
        self.assertTrue(board.add_token(Point(2, 1), 'x'))
        self.assertTrue(board.add_token(Point(4, 0), 'x'))
        self.assertTrue(board.add_token(Point(4, 2), 'o'))
        self.assertTrue(board.add_token(Point(0, 2), 'u'))
#         print(board)
        self.assertEqual(board.column_count, w)
        self.assertEqual(board.row_count, h)

    def test_init_1_1(self):
        '''
        Test construction parameter and consistency with properties
        '''
        board = Board(1, 1)
        self.assertEqual(board._cell_free_count, 1)
        self.assertTrue(board.has_free_cell())
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

        with self.assertRaises(IndexError):
            board.add_token(Point(3, 0), "X")

        with self.assertRaises(IndexError):
            board.add_token(Point(3, 5), "X")

        with self.assertRaises(IndexError):
            board.add_token(Point(0, 5), "X")

    def test_undo(self):
        board = Board(4, 2)
        token = "X"

        # Add 2 token
        self.assertTrue(board.add_token(Point(0, 0), token))
        self.assertTrue(board.add_token(Point(1, 0), token))
        self.assertEqual(board.cell_used_count, 2)

        # Undo last one
        board.undo(Point(1, 0))
        self.assertEqual(board.cell_used_count, 1)

        # Check value in grid
        self.assertEqual(board.grid[0][0], token)
        self.assertEqual(board.grid[0][1], None)

    def test_get_row(self):
        import numpy as np
        w, h = 5, 3
        board = Board(w, h)
        # len
        self.assertEqual(len(board.get_row(0)), w)

        # Default to None
        a = [None for i in range(w)]
        self.assertTrue(np.array_equal(board.get_row(0), a))

        # Insert
        a[4] = 'x'
        board.add_token(Point(4, 0), 'x')
        self.assertTrue(np.array_equal(board.get_row(0), a))

        # Exception
        board.get_row(0)
        board.get_row(1)
        board.get_row(2)

        with self.assertRaises(IndexError):
            board.get_row(3)

    def test_get_column(self):
        import numpy as np
        w, h = 5, 3
        board = Board(w, h)
        # Len
        self.assertEqual(len(board.get_column(0)), h)

        # Default to None
        a = [None for i in range(h)]
        self.assertTrue(np.array_equal(board.get_column(0), a))

        # Insert
        a[2] = 'x'
        board.add_token(Point(0, 2), 'x')
        self.assertTrue(np.array_equal(board.get_column(0), a))

        # Exception
        board.get_column(0)
        board.get_column(1)
        board.get_column(2)
        board.get_column(3)
        board.get_column(4)

        with self.assertRaises(IndexError):
            board.get_row(5)

    def test_get_diag_down(self):
        '''
        00|10|20|30|40|
        01|11|21|31|41|
        02|12|22|32|42|
        '''
        import numpy as np
        w, h = 5, 3
        board = Board(w, h)
        for y in range(h):
            for x in range(w):
                board.add_token(Point(x, y), str(x) + str(y))

        line = board.get_diag_down(0, 0)
        self.assertTrue(np.array_equal(line, ['00', '11', '22']))

        line = board.get_diag_down(3, 0)
        self.assertTrue(np.array_equal(line, ['30', '41']))

        line = board.get_diag_down(4, 2)
        self.assertTrue(np.array_equal(line, ['20', '31', '42']))

        line = board.get_diag_down(0, 1)
        self.assertTrue(np.array_equal(line, ['01', '12']))

        line = board.get_diag_down(1, 2)
        self.assertTrue(np.array_equal(line, ['01', '12']))

    def test_get_diag_up(self):
        '''
        00|10|20|
        01|11|21|
        02|12|22|
        03|13|23|
        04|14|24|

        04|14|24|
        03|13|23|
        02|12|22|
        01|11|21|
        00|10|20|
        '''
        import numpy as np
        w, h = 3, 5
        board = Board(w, h)
        for y in range(h):
            for x in range(w):
                board.add_token(Point(x, y), str(x) + str(y))

        line = board.get_diag_up(0, 4)
        self.assertTrue(np.array_equal(line, ['04', '13', '22']))

        line = board.get_diag_up(0, 3)
        self.assertTrue(np.array_equal(line, ['03', '12', '21']))

        line = board.get_diag_up(0, 2)
        self.assertTrue(np.array_equal(line, ['02', '11', '20']))

        line = board.get_diag_up(0, 1)
        self.assertTrue(np.array_equal(line, ['01', '10']))

        line = board.get_diag_up(1, 4)
        self.assertTrue(np.array_equal(line, ['14', '23']))

        line = board.get_diag_up(2, 4)
        self.assertTrue(np.array_equal(line, ['24']))

        line = board.get_diag_up(1, 1)
        self.assertTrue(np.array_equal(line, ['02', '11', '20']))

    def test_anti_diag(self):
        import numpy as np
        w, h = 5, 3
        board = Board(w, h)
        for y in range(h):
            for x in range(w):
                board.add_token(Point(x, y), str(x) + str(y))

        line = np.flipud(board._grid).diagonal(0)
        self.assertTrue(np.array_equal(line, ['02', '11', '20']))

        line = np.flipud(board._grid).diagonal(1)
        self.assertTrue(np.array_equal(line, ['12', '21', '30']))

        line = np.flipud(board._grid).diagonal(-1)
        self.assertTrue(np.array_equal(line, ['01', '10']))

    def test_diag_coordinate(self):
        '''
        00|10|20|30|40|
        01|11|21|31|41|
        02|12|22|32|42|
        '''
        h = 3

        def get_origin(x, y):
            while x >= 1 and y < h - 1:
                x, y = x - 1, y + 1
            return x, y

        self.assertEqual(get_origin(1, 0), (0, 1))
        self.assertEqual(get_origin(2, 1), (1, 2))
        self.assertEqual(get_origin(4, 1), (3, 2))
        self.assertEqual(get_origin(4, 2), (4, 2))
        self.assertEqual(get_origin(0, 0), (0, 0))
        self.assertEqual(get_origin(3, 1), (2, 2))
        self.assertEqual(get_origin(2, 2), (2, 2))

    def test_equal_array(self):
        import numpy as np
        a = [1, 1, 1]
        b = [1, 1, 1]
        c = [0, 0, 0]
        d = np.full(3, 1)
        self.assertTrue(Board.array_equal(a, b))
        self.assertFalse(Board.array_equal(a, c))
        self.assertTrue(Board.array_equal(a, d))

    def test_check_line_horizontal(self):

        w, h = 5, 3
        board = Board(w, h)
        token = 'x'

        # Check empty row
        for y in range(h):
            self.assertTrue(board.check_line_horizontal(0, y, [None]))
            self.assertTrue(board.check_line_horizontal(1, y, [None, None]))
            self.assertFalse(board.check_line_horizontal(2, y, [token]))
            self.assertTrue(board.check_line_horizontal(3, y, [None, None]))

        # |-|x|-|x|-|
        self.assertTrue(board.add_token(Point(1, 1), token))
        self.assertTrue(board.add_token(Point(3, 1), token))
        self.assertTrue(board.check_line_horizontal(1, 1, [token]))
        self.assertTrue(board.check_line_horizontal(3, 1, [token]))
        self.assertTrue(board.check_line_horizontal(
            1, 1, [token, None, token]))
        self.assertTrue(board.check_line_horizontal(
            2, 1, [token, None, token]))
        self.assertTrue(board.check_line_horizontal(
            3, 1, [token, None, token]))
        self.assertFalse(board.check_line_horizontal(2, 1, [token, token]))

        # |-|x|x|x|-|
        self.assertTrue(board.add_token(Point(2, 1), token))
        self.assertTrue(board.check_line_horizontal(
            2, 1, [token, token, token]))
        self.assertTrue(board.check_line_horizontal(
            3, 1, [token, token, token]))
        self.assertTrue(board.check_line_horizontal(
            1, 1, [token, token, token]))

#     def test_get_diag_down(self):
#         board = Board(5, 4)
#         token = 'x'
#
#         # diag start at 0,0
#         board.add_token(Point(0, 0), token)
#         board.add_token(Point(1, 1), token)
#         board.add_token(Point(2, 2), token)
#         board.add_token(Point(3, 3), token)
#
#         self.assertEqual(board.get_diag_down(0, 0, 1), [token])
#         self.assertEqual(board.get_diag_down(0, 0, 2), [token, token])
#         self.assertEqual(board.get_diag_down(0, 0, 3), [token, token, token])
#         self.assertEqual(board.get_diag_down(0, 0, 4),
#                          [token, token, token, token])
#
#         # diag start at 1,2
#         board = Board(5, 4)
#         board.add_token(Point(1, 2), token)
#         board.add_token(Point(2, 3), token)
#         board.add_token(Point(3, 4), token)
#         self.assertEqual(board.get_diag_down(1, 2, 1), [token])
#         self.assertEqual(board.get_diag_down(1, 2, 2), [token, token])
#         self.assertEqual(board.get_diag_down(2, 3, 1), [token])


if __name__ == '__main__':
    unittest.main()
