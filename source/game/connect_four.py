#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from game_base.bitboard import BitBoard
from game_base.board import Token
from game_base.player import Player


class ConnectFour():

    _COLUMN = 7  # X
    _ROW = 6  # Y

    _LINE_WIN_SIZE = 4

    def __init__(self, p1=None, p2=None):
        self._board = BitBoard()
        self._p1 = p1 if not p1 is None else Player("Player 1", Token.A)
        self._p2 = p2 if not p2 is None else Player("Player 2", Token.B)
        self._winner_player = None
        self._is_over = False
        self._moves = [i for i in range(ConnectFour._COLUMN)]

    @property
    def bitboard(self):
        return self._board._bitboard

    @property
    def is_over(self):
        return self._is_over

    @property
    def current_player(self):
        return self._p1 if self._board.currentPlayer == 0 else self._p2

    @property
    def winner(self):
        return self._winner_player

    @property
    def history(self):
        return self._board._moves

    def generate_moves(self):
        '''
        @brief All legal moves
        @details Removing move from full column does not improve performances
        '''
        return self._board.listMoves()

    def is_valid_move(self, move):
        if self._is_over:
            return False

        if move not in self._board.listMoves():
            return False

        return True

    def play(self, move):
        current_player = self._board.currentPlayer
        self._board.makeMove(move)
        self._compute_ending(current_player)

    def undo(self):
        self._board.undoMove()
        self._winner_player = None
        self._is_over = False

    def _compute_ending(self, current_player):
        '''
        Decide if a game is over
        '''
        if self._board._counter < (ConnectFour._LINE_WIN_SIZE * 2) - 1:
            return False

        has_winner = self._board.isWin(current_player)

        if has_winner:
            self._winner_player = self._p1 if current_player == 0 else self._p2

        self._is_over = not self._board.hasFreeCell() or has_winner
        return self._is_over
