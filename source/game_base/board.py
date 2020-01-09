#!/usr/bin/env python3
# -*- coding: utf-8 -*-


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

    def __init__(self, column_count, row_count):
        '''
        @todo Try with Numpy array for better performance ?
        '''

        self._column = column_count  # X
        self._row = row_count        # Y

        self._grid = [[None for x in range(self._column)]
                      for y in range(self._row)]

        self._cell_free_count = self._column * self._row

    def has_free_cell(self):
        return self._cell_free_count > 0

    @property
    def cell_used_count(self):
        return self._column * self._row - self._cell_free_count

    @property
    def grid(self):
        return self._grid

    def add_token(self, point, token):
        '''
        @brief Add token at point coordinate
        @param[in] point, (x,y) coordinate
        @param[in] token to add
        @warning Grid coordinate are reversed (y,x)
        '''
        x, y = point.x, point.y

        if 0 > x or x >= self._column or 0 > y or y >= self._row:
            return False

        # Check free cell
        if self._grid[y][x] is not None:
            return False

        # Add token to grid
        self._grid[y][x] = token
        self._cell_free_count -= 1

        return True

    def drop_token(self, x, token):
        pass

    def undo(self, point):
        x, y = point.x, point.y

        if 0 > x or x >= self._column or 0 > y or y >= self._row:
            return False

        self._grid[y][x] = None
        self._cell_free_count += 1

        return True

    def check_line_horizontal(self, x_start, x_end, y, line_test):
        row = self._grid[y]
        return self._check_line(row, x_start, x_end, line_test)

    def check_line_vertical(self, y_start, y_end, x, line_test):
        column = [self._grid[y][x] for y in range(self._row)]
        return self._check_line(column, y_start, y_end, line_test)

    def _check_line(self, line, start, end, pattern):
        '''
        @brief Check if line_test is present in row y between start and end
        @todo Explain bound check (built-in list ?)
        '''
        length = len(pattern)
        for x in range(start, end):
            if line[x:x + length] == pattern:
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
