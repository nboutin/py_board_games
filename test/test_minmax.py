'''
Created on Jan 4, 2020

@author: nbout
'''
import unittest
import sys
import os
sys.path.insert(0, os.path.join(sys.path[0], 'source'))

from tictactoe.player import Player
from tictactoe.board import (Token, Point)
from tictactoe.tictactoe import TicTacToe
from ai.minmax import Minmax

class TestMinmax(unittest.TestCase):
        
    def test_is_leaf(self):
        ai_player = Player("AI_1", Token.CROSS, True)
        game = TicTacToe(p1 = ai_player)
        minmax = Minmax(ai_player, 7)
        
        self.assertFalse(minmax._is_leaf(game, 1))
        self.assertTrue(minmax._is_leaf(game, 0))
        
        game.play(Point(0,0))
        game.play(Point(0,1))
        game.play(Point(1,0))
        game.play(Point(1,1))
        game.play(Point(2,0))
        self.assertTrue(minmax._is_leaf(game, 1))
        self.assertTrue(minmax._is_leaf(game, 0))

    def test_evaluate(self):

        ai_player = Player("AI_1", Token.CROSS, True)
        game = TicTacToe(p1 = ai_player)
        minmax = Minmax(ai_player, 7)
        
        self.assertEqual(minmax._evaluate(game, Token.CROSS), 0)
        self.assertEqual(minmax._evaluate(game, Token.CIRCLE), 0)
        
        game.play(Point(0,0))
        game.play(Point(0,1))
        game.play(Point(1,0))
        game.play(Point(1,1))
        game.play(Point(2,0))
        
        self.assertEqual(minmax._evaluate(game, Token.CROSS), Minmax.WIN_POINT)
        self.assertEqual(minmax._evaluate(game, Token.CIRCLE), Minmax.LOOSE_POINT)
        
        
    def test_minmax_d0(self):
        '''
        XX-
        OO-
        XO-
        '''
        ai_player = Player("AI_1", Token.CROSS, True)
        game = TicTacToe(p1 = ai_player)
        minmax = Minmax(ai_player, 7)
        depth = 0
 
        game.play(Point(0,0))
        game.play(Point(0,1))
        game.play(Point(1,0))
        game.play(Point(1,1))
        game.play(Point(0,2))
        game.play(Point(1,2))
        
        game.play(Point(2,0))
        self.assertEqual(minmax._minmax(game, depth, False), Minmax.WIN_POINT)
        game.undo()

        game.play(Point(2,1))
        self.assertEqual(minmax._minmax(game, depth, False), Minmax.DRAW_POINT)
        game.undo()

        game.play(Point(2,2))
        self.assertEqual(minmax._minmax(game, depth, False), Minmax.DRAW_POINT)
        game.undo()

    def test_minmax_d1(self):
        '''
        XX-
        OO-
        XO-
        '''
        ai_player = Player("AI_1", Token.CROSS, True)
        game = TicTacToe(p1 = ai_player)
        minmax = Minmax(ai_player, 7)
        depth = 1
 
        game.play(Point(0,0))
        game.play(Point(0,1))
        game.play(Point(1,0))
        game.play(Point(1,1))
        game.play(Point(0,2))
        game.play(Point(1,2))
        
        game.play(Point(2,0))
        self.assertEqual(minmax._minmax(game, depth, False), Minmax.WIN_POINT)
        game.undo()

        game.play(Point(2,1))
        self.assertEqual(minmax._minmax(game, depth, False), Minmax.DRAW_POINT)
        game.undo()

        game.play(Point(2,2))
        self.assertEqual(minmax._minmax(game, depth, False), Minmax.LOOSE_POINT)
        game.undo()
        
    def test_minmax_d2(self):
        ''' O|-|X
            X|X|O
            O|-|-
        '''
        ai_player = Player("AI_1", Token.CROSS, True)
        game = TicTacToe(p1 = ai_player)
        minmax = Minmax(ai_player, 7)
        depth = 2
        
        game.play(Point(2,0))
        game.play(Point(0,0))
        game.play(Point(0,1))
        game.play(Point(0,2))
        game.play(Point(1,1))
        game.play(Point(2,1))
        
        game.play(Point(1,0))
        self.assertEqual(minmax._minmax(game, depth, False), Minmax.DRAW_POINT)
        game.undo()

        game.play(Point(1,2))
        self.assertEqual(minmax._minmax(game, depth, False), Minmax.DRAW_POINT)
        game.undo()
        
    def test_minmax(self):
        '''
        X|-|-
        -|-|-
        -|-|-
        '''
        pass
        

if __name__ == "__main__":
    unittest.main()