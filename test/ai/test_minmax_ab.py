#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
import sys
import os
import time
sys.path.insert(0, os.path.join(sys.path[0], 'source'))
# sys.path.insert(0, os.path.join(sys.path[0], '..', '..', 'source'))


from game_base.board import (Point, Board, Token)
from game_base.player import Player
from ai.minmax_ab import Minmax_AB
from game.tictactoe import TicTacToe


class TestMinmaxAB(unittest.TestCase):

    def test_is_leaf(self):
        ai_player = Player("AI_1", Token.A, True)
        game = TicTacToe(p1=ai_player)
        minmax = Minmax_AB(ai_player, 7)

        self.assertFalse(minmax._is_leaf(game, 1))
        self.assertTrue(minmax._is_leaf(game, 0))

        game.play(Point(0, 0))
        game.play(Point(0, 1))
        game.play(Point(1, 0))
        game.play(Point(1, 1))
        game.play(Point(2, 0))
        self.assertTrue(minmax._is_leaf(game, 1))
        self.assertTrue(minmax._is_leaf(game, 0))

    def test_evaluate_d0(self):
        '''
        X|X|X
        O|O|-
        -|-|-
        '''

        ai_player = Player("AI_1", Token.A, True)
        game = TicTacToe(p1=ai_player)
        minmax = Minmax_AB(ai_player, 7)
        depth = 0

        self.assertEqual(minmax._evaluate(
            game, depth, Token.A), Minmax_AB.DRAW_POINT)
        self.assertEqual(minmax._evaluate(
            game, depth, Token.B), Minmax_AB.DRAW_POINT)

        game.play(Point(0, 0))
        game.play(Point(0, 1))
        game.play(Point(1, 0))
        game.play(Point(1, 1))
        game.play(Point(2, 0))

        self.assertEqual(minmax._evaluate(
            game, depth, Token.A), Minmax_AB.WIN_POINT)

        self.assertEqual(minmax._evaluate(
            game, depth, Token.B), Minmax_AB.LOOSE_POINT)

    def test_evaluate_d1(self):
        '''
        X|X|X
        O|O|-
        -|-|-
        '''
        ai_player = Player("AI_1", Token.A, True)
        game = TicTacToe(p1=ai_player)
        minmax = Minmax_AB(ai_player, 7)
        depth = 10

        self.assertEqual(minmax._evaluate(
            game, depth, Token.A), Minmax_AB.DRAW_POINT)

        self.assertEqual(minmax._evaluate(
            game, depth, Token.B), Minmax_AB.DRAW_POINT)

        game.play(Point(0, 0))
        game.play(Point(0, 1))
        game.play(Point(1, 0))
        game.play(Point(1, 1))
        game.play(Point(2, 0))

        self.assertEqual(minmax._evaluate(
            game, depth, Token.A), Minmax_AB.WIN_POINT + depth)

        self.assertEqual(minmax._evaluate(
            game, depth, Token.B), Minmax_AB.LOOSE_POINT - depth)

    def test_minmax_d1(self):
        '''
        XX-
        OO-
        XO-
        Simulate max loop and calling min evaluation
        '''
        ai_player = Player("AI_1", Token.A, True)
        game = TicTacToe(p1=ai_player)
        depth = 1
        minmax = Minmax_AB(ai_player, depth)

        game.play(Point(0, 0))
        game.play(Point(0, 1))
        game.play(Point(1, 0))
        game.play(Point(1, 1))
        game.play(Point(0, 2))
        game.play(Point(1, 2))

        game.play(Point(2, 0))
        val, _ = minmax._min_alpha_beta(game, depth, -1000, 1000)
        self.assertEqual(val, Minmax_AB.WIN_POINT + depth)
        game.undo()

        game.play(Point(2, 1))
        val, _ = minmax._min_alpha_beta(game, depth, -1000, 1000)
        self.assertEqual(val, Minmax_AB.DRAW_POINT)
        game.undo()

        game.play(Point(2, 2))
        val, _ = minmax._min_alpha_beta(game, depth, -1000, 1000)
        self.assertEqual(val, Minmax_AB.LOOSE_POINT)
        game.undo()

    def test_minmax_d2(self):
        ''' 
        O|-|X
        X|X|O
        O|-|-
        '''
        ai_player = Player("AI_1", Token.A, True)
        game = TicTacToe(p1=ai_player)
        depth = 2
        minmax = Minmax_AB(ai_player, depth)

        game.play(Point(2, 0))
        game.play(Point(0, 0))
        game.play(Point(0, 1))
        game.play(Point(0, 2))
        game.play(Point(1, 1))
        game.play(Point(2, 1))

        game.play(Point(1, 0))
        val, _ = minmax._min_alpha_beta(game, depth, -1000, 1000)
        self.assertEqual(val, Minmax_AB.DRAW_POINT)
        game.undo()

        game.play(Point(1, 2))
        val, _ = minmax._min_alpha_beta(game, depth, -1000, 1000)
        self.assertEqual(val, Minmax_AB.DRAW_POINT)
        game.undo()


if __name__ == '__main__':
    unittest.main()
