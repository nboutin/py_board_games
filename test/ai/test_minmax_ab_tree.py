#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
import sys
import os
sys.path.insert(0, os.path.join(sys.path[0], 'source'))
# sys.path.insert(0, os.path.join(sys.path[0], '..', '..', 'source'))


from game_base.board import (Point, Board)
from game_base.player import Player
from game.connect_four import (ConnectFour, Token)
from ai.minmax_alphabeta_tree import Minmax_AlphaBeta_Tree

@unittest.skip("not supported")
class TestMinmaxAlphaBetaTree(unittest.TestCase):

    @unittest.skip("")
    def test_export_json(self):

        depth = 4
        p1 = Player("AI_1", Token.A, True)
        minmax = Minmax_AlphaBeta_Tree(p1, depth)
        game = ConnectFour(p1=p1)
        minmax.compute(game)

        minmax.to_json("minmax" + str(depth) + ".json")

    @unittest.skip("")
    def test_print_and_export(self):
        p1 = Player("AI_1", Token.A, True)
        minmax = Minmax_AlphaBeta_Tree(p1, 3)
        game = ConnectFour(p1=p1)
        minmax.compute(game)

#         print(minmax)
        minmax.to_picture()


if __name__ == '__main__':
    unittest.main()
