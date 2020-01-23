#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
import timeit

import sys
import os
sys.path.insert(0, os.path.join(sys.path[0], 'source'))

from game_base.board import Board

# @unittest.skip("timeit")


class TestPerfoBoard(unittest.TestCase):

    def test_board_array_equal(self):

        setup = '''
from game_base.board import Board
a = ['x' for _ in range(10)]
b = ['o' for _ in range(10)]
'''
        stmt = '''
Board.array_equal(a,b)
Board.array_equal(a,a)
'''
        print("board:", timeit.timeit(setup=setup, stmt=stmt, number=100000))

    def test_numpy_array_equal(self):

        setup = '''
import numpy as np
a = np.full(10, 'x')
b = np.full(10, 'o')
'''
        stmt = '''
np.array_equal(a,b)
np.array_equal(a,a)
'''
        print("numpy:", timeit.timeit(setup=setup, stmt=stmt, number=100000))


if __name__ == "__main__":
    #     import sys, os;
    #     sys.path.insert(0, os.path.join(sys.path[0], 'source'))
    #     sys.argv = ['', 'Test.testName', os.path.join(sys.path[0], 'source')]
    unittest.main()
