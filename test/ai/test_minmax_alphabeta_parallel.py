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
from ai.minmax_alphabeta_thread import Minmax_AlphaBeta_Thread
from game.tictactoe import TicTacToe


class TestMinmaxAlphaBeta(unittest.TestCase):

    def test_A(self):
        ai_player = Player("AI_1", Token.A, True)
        game = TicTacToe(p1=ai_player)
        depth = 9
        minmax = Minmax_AlphaBeta_Thread(ai_player, depth)

        minmax.compute(game)

if __name__ == "__main__":
    unittest.main()