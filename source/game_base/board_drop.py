#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from game_base.board import (Board, Point)


class BoardDrop(Board):

    def __init__(self, column_count, row_count):
        super().__init__(column_count, row_count)

        self._cell_free_column_count = [row_count for _ in range(column_count)]

    def is_column_full(self, x):
        return self._cell_free_column_count[x] <= 0

    def add_token(self, point, token):
        raise Exception("Not Implemented")

    def drop_token(self, x, token):
        '''
        @brief Drop token in column x
        @param[in] x column coordinate
        @param[in] token to drop
        @warning Grid coordinate are reversed (y,x)
        '''

        if 0 > x or x >= self._column_count:
            return False

        y = self._cell_free_column_count[x] - 1

        if not super().add_token(Point(x, y), token):
            return False

        self._cell_free_column_count[x] -= 1

        return True

    def undo(self, x=None):

        point = None
        if x is not None:
            y = self._cell_free_column_count[x]
            point = Point(x, y)

        if not super().undo(point):
            return False

        self._cell_free_column_count[x] += 1

        return True
