#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import time

from game_base.board import (Point)


class Minmax():

    __MOVES = [Point(0, 0), Point(1, 0), Point(2, 0),
               Point(0, 1), Point(1, 1), Point(2, 1),
               Point(0, 2), Point(1, 2), Point(2, 2)]

    WIN_POINT = 10
    LOOSE_POINT = -WIN_POINT
    DRAW_POINT = 0

    def __init__(self, player, depth):
        '''
        @param player: AI player
        @param depth: explore tree moves until depth value (min:1)
        '''
        self._player = player
        self._depth = depth
        self._computation_time = 0.0

    @property
    def computation_time(self):
        return self._computation_time

    def compute(self, game):
        best_move = None
        depth = self._depth

        start = time.time()
        _, best_move = self._max(game, depth)

        end = time.time()
        self._computation_time = round(end - start, 3)

        return best_move

    def _max(self, game, depth):

        max = -sys.maxsize - 1
        best_move = None

        if self._is_leaf(game, depth):
            return self._evaluate(game, depth,  self._player.token), best_move

        for move in Minmax.__MOVES:
            if game.play(move):
                val, _ = self._min(game, depth - 1)
                if val > max:
                    max = val
                    best_move = move
            game.undo()
        return max, best_move

    def _min(self, game, depth):

        min = sys.maxsize
        best_move = None

        if self._is_leaf(game, depth):
            return self._evaluate(game, depth,  self._player.token), best_move

        for move in Minmax.__MOVES:
            if game.play(move):
                val, _ = self._max(game, depth - 1)
                if val < min:
                    min = val
                    best_move = move
            game.undo()
        return min, best_move

    def _is_leaf(self, game, depth):
        return game.is_over or depth <= 0

    def _evaluate(self, game, depth, win_token):
        '''
        TODO: replace win_token with is_max boolean that way 
        draw point could be evaluate in function of depth
        TODO: use free cell count to improve draw value
        '''
        if game.is_over and not game.winner is None:
            if game.winner.token == win_token:
                return Minmax.WIN_POINT + depth
            else:
                return Minmax.LOOSE_POINT - depth
        return Minmax.DRAW_POINT
