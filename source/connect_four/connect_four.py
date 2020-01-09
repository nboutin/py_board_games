#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from game_base.board_drop import (BoardDrop)
from game_base.player import Player


from enum import Enum


class Token(Enum):
    BLUE = 1
    RED = 2


class ConnectFour():

    _COLUMN = 7  # X
    _ROW = 6  # Y

    _LINE_WIN_LEN = 4
    _PATTERNS = [[token for i in range(4)]
                 for token in [Token.BLUE, Token.RED]]

    def __init__(self, p1=None, p2=None):
        self._board = BoardDrop(ConnectFour._COLUMN, ConnectFour._ROW)
        self._p1 = p1 if not p1 is None else Player("Player 1", Token.BLUE)
        self._p2 = p2 if not p2 is None else Player("Player 2", Token.RED)
        self._current_player = self._p1
        self._winner_player = None
        self._is_over = False
        self._moves = list()

    @property
    def grid(self):
        return self._board.grid

    @property
    def is_over(self):
        return self._is_over

    @property
    def current_player(self):
        return self._current_player

    @property
    def winner(self):
        return self._winner_player

    @property
    def history(self):
        return self._moves

    def play(self, move):
        if self._is_over:
            self._moves.append(None)    # bad move
            return False

        if not self._board.drop_token(move, self._current_player.token):
            self._moves.append(None)    # bad move
            return False

        self._moves.append(move)
        self._compute_ending()
        self._compute_next_player()

        return True

    def undo(self):
        move = self._moves.pop()
        if not move is None:
            self._board.undo(move)
            self._compute_next_player()
        self._winner_player = None
        self._is_over = False

    def _compute_next_player(self):
        if self._current_player == self._p1:
            self._current_player = self._p2
        elif self._current_player == self._p2:
            self._current_player = self._p1
        else:
            assert False

    def _compute_ending(self):
        '''
        Decide if a game is over
        '''

        # todo: explain magic number
        if self._board.cell_used_count < 7:
            return False

        # Horizontal
        has_winner, token = self._has_winner_horizontal(self._board)

        # Vertical
        if not has_winner:
            has_winner, token = self._has_winner_vertical(self._board)

        # Diagonal
        if not has_winner:
            has_winner, token = self._has_winner_diagonal(self._board)

        if has_winner:
            self._winner_player = self._p1 if token == self._p1.token else self._p2

        self._is_over = not self._board.has_free_cell() or has_winner
        return self._is_over

    def _has_winner_horizontal(self, board):
        '''
        @todo: improve by using last move y value to limit scope of search
        '''
        x_min = 0
        x_max = ConnectFour._COLUMN

        for y in range(ConnectFour._ROW):

            for pattern in ConnectFour._PATTERNS:
                if board.check_line_horizontal(x_min, x_max, y, pattern):
                    return True, pattern[0]

        return False, None

    def _has_winner_vertical(self, board):
        '''
        @todo: improve by using last move x value to limit scope of search
        '''
        y_min = 0
        y_max = ConnectFour._ROW

        for x in range(ConnectFour._COLUMN):

            for pattern in ConnectFour._PATTERNS:
                if board.check_line_vertical(y_min, y_max, x, pattern):
                    return True, pattern[0]

        return False, None

    def _has_winner_diagonal(self, board):

        has_winner, token = self._has_winner_diag_down(board)

        if has_winner:
            return has_winner, token
        else:
            return self._has_winner_diag_up(board)

    def _has_winner_diag_down(self, board):
        '''
        @brief '\'
        '''
        x_max = self._COLUMN - self._LINE_WIN_LEN + 1
        y_max = self._ROW - self._LINE_WIN_LEN + 1

        for x in range(0, x_max):
            for y in range(0, y_max):
                for pattern in ConnectFour._PATTERNS:
                    line = board.get_diag_down(x, y, self._LINE_WIN_LEN)
                    if line == pattern:
                        return True, pattern[0]

        return False, None

    def _has_winner_diag_up(self, board):
        '''
        @brief '/'
        '''
        x_min = self._LINE_WIN_LEN - 1
        x_max = self._COLUMN
        y_max = self._ROW - self._LINE_WIN_LEN + 1

        for x in range(x_min, x_max):
            for y in range(0, y_max):
                for pattern in ConnectFour._PATTERNS:
                    if board.get_diag_up(x, y, self._LINE_WIN_LEN) == pattern:
                        return True, pattern[0]

        return False, None
