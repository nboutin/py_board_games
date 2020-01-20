#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from enum import (Enum, auto)
import numpy as np
from builtins import staticmethod


class Point():

    def __init__(self, x=0, y=0):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def point(self):
        return (self._x, self._y)

    def __str__(self):
        return "({},{})".format(self._x, self._y)

    def __repr__(self):
        return "({},{})".format(self._x, self._y)

    def __eq__(self, other):
        return (self._x == other._x) and (self._y == other._y)

    def __hash__(self):
        '''necessary for instances to behave sanely in dicts and sets'''
        return hash((self._x, self._y))


class Token(auto):
    A = 1
    B = 2


class Board():
    '''
    https://docs.scipy.org/doc/numpy/reference/arrays.html
    '''

    def __init__(self, width, height):
        self._grid = np.full((height, width), None)
        self._cell_free_count = self._grid.size
        self._moves = list()

    @property
    def column_count(self):
        return self._grid.shape[1]

    @property
    def row_count(self):
        return self._grid.shape[0]

    @property
    def cell_used_count(self):
        return self._grid.size - self._cell_free_count

    @property
    def grid(self):
        return self._grid

    @property
    def last_move(self):
        return self._moves[-1]

    def has_free_cell(self):
        return self._cell_free_count > 0

    def add_token(self, point, token):
        '''
        @brief Add token at point coordinate
        @param[in] point, (x,y) coordinate
        @param[in] token to add
        @warning Grid coordinate are reversed (y,x)
        '''
        x, y = point.point

        if x < 0 or y < 0:
            return False

        # Check free cell
        if self._grid[y][x] is not None:
            return False

        # Add token to grid
        self._grid[y][x] = token
        self._cell_free_count -= 1
        self._moves.append(point)

        return True

    def undo(self, point):
        '''
        @param[in] point to undo
        '''
        x, y = point.point

        if x < 0 or y < 0:
            return False

        self._grid[y][x] = None
        self._cell_free_count += 1
        self._moves.pop()

        return True

    def get_row(self, y):
        return self._grid[y, :]

    def get_column(self, x):
        return self._grid[:, x]

    def get_diag_down(self, x, y):
        x, y = (x - y, 0) if x >= y else (0, y - x)
        k = x if y == 0 else -y
        return self._grid.diagonal(k)

    def get_diag_up(self, x, y):
        # Get diag up origin point (left, down)
        h = self.row_count
        while x >= 1 and y < h - 1:
            x, y = x - 1, y + 1

        k = -(h - y - 1) if x == 0 else x
        return np.flipud(self._grid).diagonal(k)

    def check_line_all(self, x, y, pattern):
        '''
        @todo call check_line_h/l/dd/du
        '''
        pass

    def check_line_horizontal(self, x, y, pattern):
        '''
        @brief Look for pattern in row y from x - len(pattern) to x + len(pattern) positions
        @return True if pattern found otherwise False
        @fixme Error with x=1, y=1
        '''
        l = len(pattern) - 1
        x_min = max(0, x - l)
        x_max = min(self.column_count, x + l + 1)
        return Board.check_line(self.get_row(y), x_min, x_max, pattern)

    def check_line_vertical(self, x, y, pattern):
        '''
        @brief Look for pattern in column x from y - len(pattern) to y + len(pattern) positions
        @return True if pattern found otherwise False
        '''
        l = len(pattern) - 1
        y_min = max(0, y - l)
        y_max = min(self.row_count, y + l + 1)
        return Board.check_line(self.get_column(x), y_min, y_max, pattern)

    def check_line_diag_down(self, x, y, pattern):
        line = self.get_diag_down(x, y)
        return Board.check_line(line, 0, len(line), pattern)

    def check_line_diag_up(self, x, y, pattern):
        line = self.get_diag_up(x, y)
        return Board.check_line(line, 0, len(line), pattern)

    @staticmethod
    def check_line(line, start, end, pattern):
        '''
        @brief Check if pattern is present in line between start and end positions
        @param line: array to search into
        @param pattern: array to find
        @return True if pattern found otherwise False
        @details Python list split has auto bound checking.
        '''
        l = len(pattern)
        for x in range(start, end):
            if (end - x) < l:
                return False
            if Board.array_equal(line[x:x + l], pattern):
                return True
        return False

    @staticmethod
    def array_equal(a, b):
        assert len(a) == len(b), (a, b)
        for i in range(len(a)):
            if a[i] != b[i]:
                return False
        return True

    def __str__(self):
        '''
        @brief string representation for debug purpose
        '''
        s = '\n'
        for row in self._grid:
            for cell in row:
                cell = cell if cell is not None else '-'
                s += "{}|".format(cell)
            s += '\n'
        return s
