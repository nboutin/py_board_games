#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import time
from random import shuffle


class Minmax_AB():

    WIN_POINT = 100
    LOOSE_POINT = -WIN_POINT
    DRAW_POINT = 0

    def __init__(self, player, depth, rand=False):
        '''
        @param player: AI player
        @param depth: explore tree moves until depth value (min:1)
        '''
        self._player = player
        self._depth = depth
        self._computation_time = 0.0
        self._move_count = 0
        self._rand = rand

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
        self._computation_time = round(end - start, 2)

        return best_move

    def _max_alpha_beta(self, game, depth, alpha, beta):

        max = -sys.maxsize - 1
        best_move = None

        if self._is_leaf(game, depth):
            return self._evaluate(game, depth,  self._player.token), best_move

        moves = game.generate_moves()
        if self._rand:
            shuffle(moves)
        for move in moves:
            self._move_count += 1
            game.play(move)
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
            return self._evaluate(game, depth, self._player.token), best_move

        moves = game.generate_moves()
        if self._rand:
            shuffle(moves)
        for move in moves:
            self._move_count += 1
            game.play(move)
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
                return Minmax_AB.WIN_POINT - game.moveCount
            else:
                return Minmax_AB.LOOSE_POINT + game.moveCount
        return Minmax_AB.DRAW_POINT
