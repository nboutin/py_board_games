#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from enum import (Enum, auto)
import numpy as np


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
        return self._grid.shape[0]

    @property
    def row_count(self):
        return self._grid.shape[1]

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

#     a[start:stop]  # items start through stop-1
#     a[start:]      # items start through the rest of the array
#     a[:stop]       # items from the beginning through stop-1
#     a[:]           # a copy of the whole array

    def get_row(self, y):
        return self._grid[y, :]

    def get_column(self, x):
        return self._grid[:, x]

#     def get_line_h(self, y, x_start, len):
#         return self._grid[y, x_start:len]
#
#     def get_line_v(self, x, y_start, len):
#         return self._grid[y_start:len, x]

    def get_diag_down(self, x, y):
        x, y = (x - y, 0) if x >= y else (0, y - x)
        return self._grid.diagonal(x)
#         return [self._grid[y + i][x + i] for i in range(len)]

    def get_diag_up(self, x, y):
        x, y = (x - y, 0) if x >= y else (0, y - x)
        return np.flipud(a).diagonal(x)
#         return [self._grid[y + i][x - i] for i in range(len)]

    def check_line_all(self, x, y, pattern):
        '''
        @todo call check_line_h/l/dd/du
        '''
        pass

    def check_line_horizontal(self, x_start, x_end, y, pattern):
        '''
        @brief Look for pattern in row y from x_start to x_end positions
        @return True if pattern found otherwise False
        @todo update param to use x,y and deduce start and end from len(pattern)
        '''
        return Board.check_line(self.get_row(y), x_start, x_end, pattern)

    def check_line_vertical(self, y_start, y_end, x, pattern):
        '''
        @brief Look for pattern in column x from y_start to y_end positions
        @return True if pattern found otherwise False
        '''
        return Board.check_line(self.get_column(x), y_start, y_end, pattern)

    def check_line_diag_down(self, x, y, pattern):
        len = len(pattern) - 1
        return Board.check_line(self.get_diag_down(x, y), x - len, x + len, pattern)

    def check_line_diag_up(self, x, y, pattern):
        len = len(pattern) - 1
        return Board.check_line(self.get_diag_up(x, y), x - len, x + len, pattern)

    @staticmethod
    def check_line(line, start, end, pattern):
        '''
        @brief Check if pattern is present in line between start and end positions
        @param line: array to search into
        @param pattern: array to find
        @return True if pattern found otherwise False
        @details Python list split has auto bound checking.
        '''
        length = len(pattern)
        for x in range(start, end):
            #             if line[x:x + length] == pattern:
            if np.array_equal(line[x:x + length], pattern):
                return True
        return False

    def __str__(self):
        '''
        @brief string representation for debug purpose
        '''
        s = '\n'
        for row in self._grid:
            for cell in row:
                s += "{}|".format(cell)
            s += '\n'
        return s
