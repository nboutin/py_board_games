#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import time

from anytree import Node, RenderTree, NodeMixin


class Minmax_AlphaBeta_Tree():

    WIN_POINT = 100
    LOOSE_POINT = -WIN_POINT
    DRAW_POINT = 0

    def __init__(self, player, depth, moves):
        '''
        @param player: AI player
        @param depth: explore tree moves until depth value (min:1)
        '''
        self._player = player
        self._depth_max = depth
        self._moves = moves
        self._computation_time = 0.0
        self._root = Node("r", val=0)

    @property
    def computation_time(self):
        return self._computation_time

    def compute(self, game):
        best_move = None
        depth_start = 1
        alpha = -sys.maxsize - 1
        beta = sys.maxsize

        start = time.time()
        _, best_move = self._max_alpha_beta(
            game, depth_start, alpha, beta, self._root)

        end = time.time()
        self._computation_time = round(end - start, 3)

        return best_move

    def _max_alpha_beta(self, game, depth, alpha, beta, parent):

        max = -sys.maxsize - 1
        best_move = None

        if self._is_leaf(game, depth):
            return self._evaluate(game, depth,  self._player.token), best_move

        for move in self._moves:
            if game.play(move):
                node = self.make_node(True, depth, move, parent, 0)

                val, _ = self._min_alpha_beta(
                    game, depth + 1, alpha, beta, node)
                node.val = val

                if val > max:
                    max = val
                    best_move = move
            game.undo()

            if max >= beta:
                return max, best_move

            if max > alpha:
                alpha = max

        return max, best_move

    def _min_alpha_beta(self, game, depth, alpha, beta, parent):

        min = sys.maxsize
        best_move = None

        if self._is_leaf(game, depth):
            return self._evaluate(game, depth, self._player.token), best_move

        for move in self._moves:
            if game.play(move):
                node = self.make_node(False, depth, move, parent, 0)

                val, _ = self._max_alpha_beta(
                    game, depth + 1, alpha, beta, node)
                node.val = val

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
        return game.is_over or depth > self._depth_max

    def _evaluate(self, game, depth, win_token):
        '''
        TODO: replace win_token with is_max boolean that way 
        draw point could be evaluate in function of depth
        TODO: use free cell count to improve draw value
        '''
        if game.is_over and not game.winner is None:
            if game.winner.token == win_token:
                return Minmax_AlphaBeta_Tree.WIN_POINT + depth
            else:
                return Minmax_AlphaBeta_Tree.LOOSE_POINT - depth
        return Minmax_AlphaBeta_Tree.DRAW_POINT

    def __str__(self):
        s = ''
        for pre, fill, node in RenderTree(self._root):
            s += '%s%s(%s)\n' % (pre, node.name, node.val)
        return s

    def make_node(self, is_max, depth, move, parent, val):
        name = '+' if is_max else '-'
        name += '{}{}'.format(parent.name[1:], move)
        return Node(name, parent=parent, val=val)

    def to_picture(self, filename="minmax.png"):
        from anytree.exporter import UniqueDotExporter
        UniqueDotExporter(self._root, nodeattrfunc=lambda n: 'label="%s"' % (
            n.name + '.' + str(n.val))).to_picture(filename)

    def to_json(self, filename='minmax.json'):
        from anytree.exporter import JsonExporter
        exporter = JsonExporter(indent=2)
        with open(filename, 'w') as file:
            exporter.write(self._root, file)
