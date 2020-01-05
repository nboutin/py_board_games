#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
from enum import Enum


class Token(Enum):
    CROSS = 1
    CIRCLE = 2


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

    __COLUMN = 3  # X
    __ROW = 3  # Y

    def __init__(self):
        '''ToDo: try with Numpy array for better performance ?'''
        
        self._grid = [[None for x in range(Board.__COLUMN)]
                      for x in range(Board.__ROW)]
        self._free_cell_count = Board.__COLUMN * Board.__ROW

    def has_free_cell(self):
        return self._free_cell_count > 0
    
    @property
    def played_cell_count(self):
        return Board.__COLUMN * Board.__ROW - self._free_cell_count

    @property
    def grid(self):
        return self._grid

    def play(self, point, token):
        ''' grid coordinate are reversed (y,x)'''
        x,y = point.x, point.y

        if 0 > x or x >= Board.__COLUMN or 0 > y or y >= Board.__ROW:
            return False

        # Check free cell
        if self._grid[y][x] is not None:
            return False

        # Add token to grid
        self._grid[y][x] = token
        self._free_cell_count -= 1

        return True

    def undo(self, point):
        x,y = point.x, point.y
        
        if 0 > x or x >= Board.__COLUMN or 0 > y or y >= Board.__ROW:
            return False

        self._grid[y][x] = None
        self._free_cell_count += 1

        return True
