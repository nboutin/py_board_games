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
        self.assertEqual(game.current_player, game._p1)

    def test_deepcopy(self):
        game = ConnectFour()
        cgame = copy.deepcopy(game)

        self.assertFalse(game is cgame)

    def test_next_player(self):
        game = ConnectFour()

        self.assertEqual(game.current_player, game._p1)
        game.play(0)
        self.assertEqual(game.current_player, game._p2)
        game.play(0)
        self.assertEqual(game.current_player, game._p1)
        game.play(0)
        self.assertEqual(game.current_player, game._p2)
        game.play(0)
        self.assertEqual(game.current_player, game._p1)
        game.play(0)
        self.assertEqual(game.current_player, game._p2)
        game.play(0)
        self.assertEqual(game.current_player, game._p1)

        # Cell not free, do not change current player
        self.assertFalse(game.is_valid_move(0))
        self.assertEqual(game.current_player, game._p1)

    def test_win_horizontal_player1(self):
        '''
        R|R|R|.
        B|B|B|B
        '''
        game = ConnectFour()

        game.play(0)
        game.play(0)
        game.play(1)
        game.play(1)
        game.play(2)
        game.play(2)
        game.play(3)

        self.assertTrue(game.is_over)
        self.assertEqual(game.winner, game._p1)

    def test_win_horizontal_player2(self):
        '''
        R|R|R|R|B
        B|B|B|R|B
        '''
        game = ConnectFour()

        game.play(0)
        game.play(0)
        game.play(1)
        game.play(1)
        game.play(2)
        game.play(2)
        game.play(4)
        game.play(3)
        game.play(4)
        game.play(3)

        self.assertTrue(game.is_over)
        self.assertEqual(game.winner, game._p2)

    def test_win_horizontal_right(self):
        '''
        .|.|.|.|R|R|R|
        .|.|.|B|B|B|B|
        '''
        game = ConnectFour()

        game.play(6)
        game.play(6)
        game.play(5)
        game.play(5)
        game.play(4)
        game.play(4)
        game.play(3)

        self.assertTrue(game.is_over)
        self.assertEqual(game.winner, game._p1)

    def test_win_vertical_player1(self):
        game = ConnectFour()

        game.play(0)
        game.play(1)
        game.play(0)
        game.play(1)
        game.play(0)
        game.play(1)
        game.play(0)

        self.assertTrue(game.is_over)
        self.assertEqual(game.winner, game._p1)

    def test_win_vertical_player2(self):
        game = ConnectFour()
        game.play(5)
        game.play(6)
        game.play(5)
        game.play(6)
        game.play(5)
        game.play(6)
        game.play(0)
        game.play(6)

        self.assertTrue(game.is_over)
        self.assertEqual(game.winner, game._p2)

    def test_win_vertical_top_middle(self):
        game = ConnectFour()
        game.play(0)
        game.play(3)
        game.play(0)
        game.play(3)

        game.play(3)
        game.play(0)
        game.play(3)
        game.play(0)
        game.play(3)
        game.play(0)
        game.play(3)

        self.assertTrue(game.is_over)
        self.assertEqual(game.winner, game._p1)

    def test_win_diag_down_player1(self):
        game = ConnectFour()
        game.play(0)
        game.play(0)
        game.play(0)
        game.play(1)

        game.play(0)  # B

        game.play(1)
        game.play(1)  # B

        game.play(2)
        game.play(2)  # B

        game.play(4)
        game.play(3)  # B

        self.assertTrue(game.is_over)
        self.assertEqual(game.winner, game._p1)

    def test_generate_moves(self):
        game = ConnectFour()
        self.assertEqual(game.generate_moves(), [0, 1, 2, 3, 4, 5, 6])

        for i in range(ConnectFour._ROW):
            game.play(0)
        for i in range(ConnectFour._ROW):
            game.play(4)
        self.assertEqual(game.generate_moves(), [1, 2, 3, 5, 6])


class TestGamePosition(unittest.TestCase):

    @unittest.skip('')
    def test_rand_move(self):
        p1 = Player("AI_1", Token.A, True)
        p2 = Player("AI_2", Token.B, True)
        ai1 = Minmax_AB(p1, 6, True)
        ai2 = Minmax_AB(p2, 2, False)
        game = ConnectFour(p1=p1, p2=p2)

        for m in [3, 0, 6, 0, 5, 4, 1, 0, 0, 0, 5, 0, 6, 1, 2, 1, 6, 6, 6, 1, 1, 1, 5, 5, 5, 2, 6, 3]:
            game.play(m)
        print(game._board)

        while not game.is_over:
            cp = game.current_player
            if cp == p1:
                move = ai1.compute(game)
            elif cp == p2:
                move = ai2.compute(game)
            else:
                self.assertTrue(False)

            game.play(move)
        print("winner", game.winner)
        print("history", game.history)
        self.assertEqual(game.winner, p1)

    def test_pos4(self):
        p1 = Player("AI_1", Token.A, True)
        ai1a = Minmax_AB(p1, 2, False)
#         ai1b = Minmax_AB(p1, 2, True)
        game = ConnectFour(p1=p1)
        for m in [3, 0, 6, 0, 5, 4, 1, 0, 0, 0, 5, 0, 6, 1, 2, 1, 6, 6, 6, 1, 1, 1, 5, 5, 5, 2]:  # 6, 3
            game.play(m)
#         print(game._board)

        self.assertFalse(game.is_valid_move(0))
        self.assertFalse(game.is_valid_move(1))
        self.assertTrue(game.is_valid_move(2))
        self.assertTrue(game.is_valid_move(3))
        self.assertTrue(game.is_valid_move(4))
        self.assertTrue(game.is_valid_move(5))
        self.assertTrue(game.is_valid_move(6))
        
        game.play(2)
        self.assertFalse(game.is_over)
        game.undo()
        
        game.play(3)
        self.assertFalse(game.is_over)
        game.undo()
        
        game.play(4)
        self.assertFalse(game.is_over)
        game.undo()

        game.play(5)
        self.assertFalse(game.is_over)
        game.undo()

        game.play(6)
        self.assertFalse(game.is_over)
        game.undo()

        self.assertEqual(game.current_player, p1)
        self.assertEqual(ai1a.compute(game), 3)
#         self.assertEqual(ai1b.compute(game), 3)

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
