#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from enum import Enum


class Token(Enum):
    CROSS = 1
    CIRCLE = 2


class Board():

    def __init__(self):
        '''
        ToDo: try with Numpy array for better performance ?
        '''
        __COLUMN = 3 # X
        __ROW = 3 # Y
        self._grid = [[None for x in range(__COLUMN)] for x in range(__ROW)]
        print (self._grid)
