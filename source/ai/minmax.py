#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

from tictactoe.board import (Point)

class Minmax():
    
    __MOVES = [Point(0,0),Point(1,0),Point(2,0),
               Point(0,1),Point(1,1),Point(2,1),
               Point(0,2),Point(1,2),Point(2,2)]
    
    def __init__(self, player, depth):
        self._player = player
        self._depth = depth
        
    def compute(self, game):
        best_move = None
        max = -sys.maxsize -1
        depth = self._depth
        
        for move in Minmax.__MOVES:
            if game.play(move):
                val = self._minmax(game, depth, False)
                if val > max:
                    max = val
                    best_move = move
            game.undo()
        return best_move
    
    def _minmax(self, game, depth, is_max):
        if self._is_leaf(game, depth):
            return self._evaluate(game, self._player.token)
        
        if not is_max:
            min = sys.maxsize
            for move in Minmax.__MOVES:
                if game.play(move):
                    val = self._minmax(game, depth - 1, True)
                    if val < min:
                        min = val
                game.undo()
            return min
        else:
            max = -sys.maxsize -1
            for move in Minmax.__MOVES:
                if game.play(move):
                    val = self._minmax(game, depth-1, False)
                    if val > max:
                        max = val
                game.undo()
            return max
        
    def _is_leaf(self, game, depth):
        return game.is_over or depth <= 0
    
    def _evaluate(self, game, win_token):
        if game.is_over and not game.winner is None:
            if game.winner.token == win_token:
                return 100
            else:
                return -100
        return 0