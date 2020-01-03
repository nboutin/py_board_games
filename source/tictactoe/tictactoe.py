#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tictactoe.board import (Token, Board)
from tictactoe.player import Player

class TicTacToe():

    def __init__(self):
        self._board = Board()
        self._p1 = Player("Player 1", Token.CROSS)
        self._p2 = Player("Player 2", Token.CIRCLE)
        self._current_player = self._p1