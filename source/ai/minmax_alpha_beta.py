#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import time

from tictactoe.board import (Point)


class Minmax_AlphaBeta():

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
        alpha = -sys.maxsize - 1
        beta = sys.maxsize

        start = time.time()
        _, best_move = self._max_alpha_beta(game, depth, alpha, beta)

        end = time.time()
        self._computation_time = round(end - start, 3)

        return best_move

    def _max_alpha_beta(self, game, depth, alpha, beta):

        max = -sys.maxsize - 1
        best_move = None

        if self._is_leaf(game, depth):
            return self._evaluate(game, depth,  self._player.token), best_move

        for move in Minmax_AlphaBeta.__MOVES:
            if game.play(move):
                val, _ = self._min_alpha_beta(game, depth - 1, alpha, beta)
                if val > max:
                    max = val
                    best_move = move
            game.undo()

            if max >= beta:
                return max, best_move

            if max > alpha:
                alpha = max

        return max, best_move

    def _min_alpha_beta(self, game, depth, alpha, beta):

        min = sys.maxsize
        best_move = None

        if self._is_leaf(game, depth):
            return self._evaluate(game, depth,  self._player.token), best_move

        for move in Minmax_AlphaBeta.__MOVES:
            if game.play(move):
                val, _ = self._max_alpha_beta(game, depth - 1, alpha, beta)
                if val < min:
                    min = val
                    best_move = move
            game.undo()

            if min <= alpha:
                return min, best_move

            if min < beta:
                beta = min

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
                return Minmax_AlphaBeta.WIN_POINT + depth
            else:
                return Minmax_AlphaBeta.LOOSE_POINT - depth
        return Minmax_AlphaBeta.DRAW_POINT
