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

    @property
    def point(self):
        return (self._x, self._y)

    def __str__(self):
        return "({},{})".format(self._x, self._y)

    def __repr__(self):
        return "({},{})".format(self._x, self._y)
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
     
    def __lt__(self, other):
         return self.y < other.y or (self.y == other.y and self.x < other.x)


class Board():

    def __init__(self, column_count, row_count):
        self._column_count = column_count  # X
        self._row_count = row_count        # Y

        self._grid = [[None for x in range(self._column_count)]
                      for y in range(self._row_count)]

        self._cell_free_count = self._column_count * self._row_count
        self._moves = list()

    @property
    def column_count(self):
        return self._column_count

    @property
    def row_count(self):
        return self._row_count

    @property
    def cell_used_count(self):
        return self._column_count * self._row_count - self._cell_free_count

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

        if 0 > x or x >= self._column_count or 0 > y or y >= self._row_count:
            return False

        # Check free cell
        if self._grid[y][x] is not None:
            return False

        # Add token to grid
        self._grid[y][x] = token
        self._cell_free_count -= 1
        self._moves.append(point)

        return True

    def drop_token(self, x, token):
        pass

    def undo(self, point=None):
        '''
        @param[in] point to undo, if None last point
        '''
        if point is None:
            point = self._moves.pop()

        x, y = point.point

        if 0 > x or x >= self._column_count or 0 > y or y >= self._row_count:
            return False

        self._grid[y][x] = None
        self._cell_free_count += 1
        self._moves.pop()

        return True

    def check_line_horizontal(self, x_start, x_end, y, line_test):
        row = self._grid[y]
        return self._check_line(row, x_start, x_end, line_test)

    def check_line_vertical(self, y_start, y_end, x, line_test):
        column = self.get_column(x, self._row_count)
        return self._check_line(column, y_start, y_end, line_test)

    def _check_line(self, line, start, end, pattern):
        '''
        @brief Check if line_test is present in row y between start and end
        @details Python list split has auto bound checking.
        '''
        length = len(pattern)
        for x in range(start, end):
            if line[x:x + length] == pattern:
                return True
        return False

    def get_column(self, x, len):
        return [self._grid[y][x] for y in range(len)]

    def get_diag_down(self, x, y, len):
        return [self._grid[y + i][x + i] for i in range(len)]

    def get_diag_up(self, x, y, len):
        return [self._grid[y + i][x - i] for i in range(len)]

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
