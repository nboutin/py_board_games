#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
import copy
import sys
import os
sys.path.insert(0, os.path.join(sys.path[0], 'source'))
# sys.path.insert(0, os.path.join(sys.path[0], '..', '..', 'source'))


from game.connect_four import (ConnectFour, Token)
from game_base.board import (Point, Board)
from game_base.player import Player
from ai.minmax_ab import Minmax_AB

class TestConnectFour(unittest.TestCase):

    def test_init(self):
        game = ConnectFour()
        self.assertFalse(game.is_over)
        self.assertEqual(game.winner, None)
        self.assertEqual(len(game.history), 0)
#         self.assertEqual(game._current_player, game._p1)

    def test_deepcopy(self):
        game = ConnectFour()
        cgame = copy.deepcopy(game)
        
        self.assertFalse(game is cgame)

#     def test_next_player(self):
#         game = ConnectFour()
# 
#         self.assertEqual(game._current_player, game._p1)
#         self.assertTrue(game.play(0))
#         self.assertEqual(game._current_player, game._p2)
#         self.assertTrue(game.play(0))
#         self.assertEqual(game._current_player, game._p1)
#         self.assertTrue(game.play(0))
#         self.assertEqual(game._current_player, game._p2)
#         self.assertTrue(game.play(0))
#         self.assertEqual(game._current_player, game._p1)
#         self.assertTrue(game.play(0))
#         self.assertEqual(game._current_player, game._p2)
#         self.assertTrue(game.play(0))
#         self.assertEqual(game._current_player, game._p1)
# 
#         # Cell not free, do not change current player
#         self.assertFalse(game.play(0))
#         self.assertEqual(game._current_player, game._p1)

    def test_win_horizontal_player1(self):
        '''
        R|R|R|.
        B|B|B|B
        '''
        game = ConnectFour()

        self.assertTrue(game.play(0))
        self.assertTrue(game.play(0))
        self.assertTrue(game.play(1))
        self.assertTrue(game.play(1))
        self.assertTrue(game.play(2))
        self.assertTrue(game.play(2))
        self.assertTrue(game.play(3))

        self.assertTrue(game.is_over)
        self.assertEqual(game.winner, game._p1)

    def test_win_horizontal_player2(self):
        '''
        R|R|R|R|B
        B|B|B|R|B
        '''
        game = ConnectFour()

        self.assertTrue(game.play(0))
        self.assertTrue(game.play(0))
        self.assertTrue(game.play(1))
        self.assertTrue(game.play(1))
        self.assertTrue(game.play(2))
        self.assertTrue(game.play(2))
        self.assertTrue(game.play(4))
        self.assertTrue(game.play(3))
        self.assertTrue(game.play(4))
        self.assertTrue(game.play(3))

        self.assertTrue(game.is_over)
        self.assertEqual(game.winner, game._p2)

    def test_win_horizontal_right(self):
        '''
        .|.|.|.|R|R|R|
        .|.|.|B|B|B|B|
        '''
        game = ConnectFour()

        self.assertTrue(game.play(6))
        self.assertTrue(game.play(6))
        self.assertTrue(game.play(5))
        self.assertTrue(game.play(5))
        self.assertTrue(game.play(4))
        self.assertTrue(game.play(4))
        self.assertTrue(game.play(3))

        self.assertTrue(game.is_over)
        self.assertEqual(game.winner, game._p1)

    def test_win_vertical_player1(self):
        game = ConnectFour()

        self.assertTrue(game.play(0))
        self.assertTrue(game.play(1))
        self.assertTrue(game.play(0))
        self.assertTrue(game.play(1))
        self.assertTrue(game.play(0))
        self.assertTrue(game.play(1))
        self.assertTrue(game.play(0))

        self.assertTrue(game.is_over)
        self.assertEqual(game.winner, game._p1)

    def test_win_vertical_player2(self):
        game = ConnectFour()
        self.assertTrue(game.play(5))
        self.assertTrue(game.play(6))
        self.assertTrue(game.play(5))
        self.assertTrue(game.play(6))
        self.assertTrue(game.play(5))
        self.assertTrue(game.play(6))
        self.assertTrue(game.play(0))
        self.assertTrue(game.play(6))

        self.assertTrue(game.is_over)
        self.assertEqual(game.winner, game._p2)

    def test_win_vertical_top_middle(self):
        game = ConnectFour()
        self.assertTrue(game.play(0))
        self.assertTrue(game.play(3))
        self.assertTrue(game.play(0))
        self.assertTrue(game.play(3))

        self.assertTrue(game.play(3))
        self.assertTrue(game.play(0))
        self.assertTrue(game.play(3))
        self.assertTrue(game.play(0))
        self.assertTrue(game.play(3))
        self.assertTrue(game.play(0))
        self.assertTrue(game.play(3))

        self.assertTrue(game.is_over)
        self.assertEqual(game.winner, game._p1)

#     def test_has_winner_diag_down(self):
#         board = Board(7, 6)
#         token = Token.A
# 
#         board.add_token(Point(0, 2), token)
#         board.add_token(Point(1, 3), token)
#         board.add_token(Point(2, 4), token)
#         board.add_token(Point(3, 5), token)
# 
#         game = ConnectFour()
#         self.assertEqual(game._has_winner_diagonal(
#             board, Point(3, 5)), (True, token))

    def test_win_diag_down_player1(self):
        game = ConnectFour()
        self.assertTrue(game.play(0))
        self.assertTrue(game.play(0))
        self.assertTrue(game.play(0))
        self.assertTrue(game.play(1))

        self.assertTrue(game.play(0))  # B

        self.assertTrue(game.play(1))
        self.assertTrue(game.play(1))  # B

        self.assertTrue(game.play(2))
        self.assertTrue(game.play(2))  # B

        self.assertTrue(game.play(4))
        self.assertTrue(game.play(3))  # B

#         print(game._board)

        self.assertTrue(game.is_over)
        self.assertEqual(game.winner, game._p1)

#     def test_win_diag_player2(self):
#         game = TicTacToe()
#         self.assertTrue(game.play(Point(0, 0)))
#         self.assertTrue(game.play(Point(0, 2)))
#         self.assertTrue(game.play(Point(1, 0)))
#         self.assertTrue(game.play(Point(1, 1)))
#         self.assertTrue(game.play(Point(0, 1)))
#         self.assertTrue(game.play(Point(2, 0)))
#
#         self.assertTrue(game.is_over)
#         self.assertEqual(game.winner, game._p2)
#
#     def test_draw(self):
#         game = TicTacToe()
#         self.assertTrue(game.play(Point(0, 0)))
#         self.assertTrue(game.play(Point(1, 0)))
#         self.assertTrue(game.play(Point(2, 0)))
#         self.assertTrue(game.play(Point(0, 1)))
#         self.assertTrue(game.play(Point(1, 1)))
#         self.assertTrue(game.play(Point(2, 2)))
#         self.assertTrue(game.play(Point(1, 2)))
#         self.assertTrue(game.play(Point(0, 2)))
#         self.assertTrue(game.play(Point(2, 1)))
#
#         self.assertTrue(game.is_over)
#         self.assertEqual(game.winner, None)

    def test_generate_moves(self):
        game = ConnectFour()
        self.assertEqual(game.generate_moves(), [0, 1, 2, 3, 4, 5, 6])

#         for i in range(ConnectFour._ROW):
#             game.play(0)
#         for i in range(ConnectFour._ROW):
#             game.play(4)
#         self.assertEqual(game.generate_moves(), [1, 2, 3, 5, 6])

class TestGamePosition(unittest.TestCase):

    def test_pos3(self):
        '''
          0 1 2 3 4 5 6
        0|X|X|-|-|-|-|-|
        1|X|O|-|-|-|-|-|
        2|O|X|-|-|-|-|-|
        3|X|O|-|-|-|-|-|
        4|O|X|O|-|-|-|-|
        5|X|O|O|-|-|-|-|
        Player_1(X) to play
        '''
        p1 = Player("AI_1", Token.A, True)
        p2 = Player("AI_2", Token.B, True)
        game = ConnectFour(p1=p1, p2=p2)

        moves = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 2, 1, 2]
        for m in moves:
            game.play(m)

        depth = 2
        ai = Minmax_AB(p1, depth)

        self.assertEqual(ai.compute(game), 3)

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
        p2 = Player("AI_2", Token.B, True)
        game = ConnectFour(p2=p2)

        moves = [3, 0, 4, 2, 3, 0, 2, 0, 0, 4, 1,
                 2, 3, 3, 1, 1, 2, 0, 0, 2, 4, 0, 4]
        for move in moves:
            game.play(move)
            
        self.assertEqual(game.current_player, p2)

        # test p1 win position
        self.assertTrue(game.is_over)
        game.undo()
        game.undo()

        # test p1 win in (1,1)
        self.assertEqual(game.current_player, p2)
        game.play(1)  # O
        game.play(1)  # X
        self.assertTrue(game.is_over)

        # p2 turn, should block (4,3)
        game.undo()
        game.undo()
        self.assertEqual(game.current_player, p2)
        depth = 2
        minmax = Minmax_AB(p2, depth)
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

        p2 = Player("AI_2", Token.B, True)
        game = ConnectFour(p2=p2)

        moves = [3, 0, 4, 2, 5, 6, 4, 0, 3, 0, 0, 2, 2, 2, 5, 6, 4, 4, 3]
        for move in moves:
            game.play(move)

        self.assertEqual(game.current_player, p2)

        depth = 1
        minmax = Minmax_AB(p2, depth)
        self.assertEqual(minmax.compute(game), 0)

        depth = 2
        minmax = Minmax_AB(p2, depth)
        self.assertEqual(minmax.compute(game), 0)

if __name__ == '__main__':
    unittest.main()
