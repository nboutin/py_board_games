#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
import sys
import os
# sys.path.insert(0, os.path.join(sys.path[0], 'source'))
sys.path.insert(0, os.path.join(sys.path[0], '..','..','source'))

print (sys.path)

from connect_four.connect_four import (ConnectFour, Token)
from ai.minmax_alpha_beta import Minmax_AlphaBeta
from game_base.player import Player

class TestGamePosition(unittest.TestCase):

    def test_pos2(self):
        '''
          0 1 2 3 4 5 6 
        0|X|-|-|-|-|-|-|
        1|O|-|O|-|-|-|-|
        2|X|-|X|O|-|-|-|
        3|O|O|O|X|X|-|-|
        4|O|X|X|X|O|-|-|
        5|O|X|O|X|X|-|-|
        '''
        p2 = Player("AI_2", Token.RED, True)
        game = ConnectFour(p2=p2)
        
        moves = [3,0,4,2,3,0,2,0,0,4,1,2,3,3,1,1,2,0,0,2,4,0,2,4]
        for move in moves:
            game.play(move)

        self.assertEqual(game._board.get_diag_up(4,2,4), [1,1,1,1])
        game.undo()
        
        depth = 2
        minmax = Minmax_AlphaBeta(p2, depth, ConnectFour._MOVES)
        self.assertEqual(minmax.compute(game), 4)

    def test_pos1(self):
        '''
          0 1 2 3 4 5 6 
        0|-|-|-|-|-|-|-|
        1|-|-|-|-|-|-|-|
        2|X|-|O|-|O|-|-|
        3|O|-|X|X|X|-|-|
        4|O|-|O|X|X|X|O|
        5|O|-|O|X|X|X|O|
        '''
        p2 = Player("AI_2", Token.RED, True)
        game = ConnectFour(p2=p2)
        
        moves = [3,0,4,2,5,6,4,0,3,0,0,2,2,2,5,6,4,4,3]
        for move in moves:
            game.play(move)
            
        depth = 1
        minmax = Minmax_AlphaBeta(p2, depth, ConnectFour._MOVES)
        self.assertEqual(minmax.compute(game), 0)

        depth = 2
        minmax = Minmax_AlphaBeta(p2, depth, ConnectFour._MOVES)
        self.assertEqual(minmax.compute(game), 0)
