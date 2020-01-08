#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from enum import Enum


class Token(Enum):
    BLUE = 1
    RED = 2


class Point():

    def __init__(self, x, y):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    def __str__(self):
        return "({},{})".format(self._x, self._y)


class Board():

    _COLUMN = 7  # X
    _ROW = 6  # Y

    def __init__(self):
        self._grid = [[None for x in range(Board._COLUMN)]
                      for x in range(Board._ROW)]
        self._cell_free_count = Board._COLUMN * Board._ROW
        self._cell_free_column_count = [
            Board._ROW for i in range(Board._COLUMN)]

    def has_free_cell(self):
        return self._cell_free_count > 0

    @property
    def cell_played_count(self):
        return Board._COLUMN * Board._ROW - self._cell_free_count

    @property
    def grid(self):
        return self._grid

    def play(self, x, token):
        ''' grid coordinate are reversed (y,x)
        @todo move free falling token to call connect_four
        '''

        if 0 > x or x >= Board._COLUMN:
            return False

        y = self._cell_free_column_count[x] - 1

        # Check free space in column
        if y < 0:
            return False

        # Let token free fall
        self._grid[y][x] = token
        self._cell_free_count -= 1
        self._cell_free_column_count[x] -= 1

        return True

    def undo(self, x):

        if 0 > x or x >= Board._COLUMN:
            return False

        y = self._cell_free_column_count[x] - 1

        self._grid[y][x] = None
        self._cell_free_count += 1
        self._cell_free_column_count[x] += 1

        return True

    def check_line_horizontal(self, x_start, x_end, y, line_test):
        '''
        check if line_test is present in row y between x_start and x_end
        @todo explain bound check (built-in list ?)
        '''
        row = self._grid[y]
        length = len(line_test)
        for x in range(x_start, x_end):
            if row[x:x + length] == line_test:
                return True
        return False

    def __str__(self):
        ''' string representation for debug purpose'''
        s = '\n'
        for row in self._grid:
            for cell in row:
                s += "{}|".format(cell)
            s += '\n'
        return s
