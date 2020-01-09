#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from game_base.board import (Board, Point)


class BoardDrop(Board):

    def __init__(self, column_count, row_count):
        super().__init__(column_count, row_count)

        self._cell_free_column_count = [self._row for i in range(self._column)]

    def add_token(self, point, token):
        raise Exception("do not use")

    def drop_token(self, x, token):
        '''
        @brief Drop token in column x
        @param[in] x column coordinate
        @param[in] token to drop
        @warning Grid coordinate are reversed (y,x)
        '''
        
        if 0 > x or x >= self._column:
            return False
        
        y = self._cell_free_column_count[x] - 1

        if not super().add_token(Point(x, y), token):
            return False

        self._cell_free_column_count[x] -= 1

        return True

    def undo(self, x):

        y = self._cell_free_column_count[x]

        if not super().undo(Point(x, y)):
            return False

        self._cell_free_column_count[x] += 1

        return True
