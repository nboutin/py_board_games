#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from game_base.board import (Board, Point)
from game_base.player import Player

from enum import Enum


class Token(Enum):
    CROSS = 1
    CIRCLE = 2


class Gomoku():

    _LINE_WIN_SIZE = 5

    def __init__(self, p1=None, p2=None, column=7, row=7):
        self._board = Board(column, row)
        self._p1 = p1 if not p1 is None else Player("Player 1", Token.CROSS)
        self._p2 = p2 if not p2 is None else Player("Player 2", Token.CIRCLE)
        assert(not(self._p1.token == self._p2.token))
        self._current_player = self._p1
        self._winner_player = None
        self._is_over = False
        self._history = list()
        self._moves = [Point(x, y) for x in range(column) for y in range(row)]
        self._patterns = [[token for i in range(Gomoku._LINE_WIN_SIZE)]
                          for token in [Token.CROSS, Token.CIRCLE]]

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
        return self._history

    def play(self, point):
        if self._is_over:
            self._history.append(None)    # bad move
            return False

        if not self._board.add_token(point, self._current_player.token):
            self._history.append(None)    # bad move
            return False

        self._history.append(point)
        self._compute_ending()
        self._compute_next_player()

        return True

    def undo(self):
        move = self._history.pop()
        if move:
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
        # todo: why minus 1 ?
        if self._board.cell_used_count < (Gomoku._LINE_WIN_SIZE * 2) - 1:
            return False

        # Horizontal
        has_winner, token = self._has_winner_horizontal(
            self._board, self._board.moves[-1].y)

        # Vertical
        if not has_winner:
            has_winner, token = self._has_winner_vertical(
                self._board, self._board.moves[-1].x)

        # Diagonal
        if not has_winner:
            has_winner, token = self._has_winner_diagonal(self._board)

        if has_winner:
            self._winner_player = self._p1 if token == self._p1.token else self._p2

        self._is_over = not self._board.has_free_cell() or has_winner
        return self._is_over

    def _has_winner_horizontal(self, board, y_last):
        x_min = 0
        x_max = self._board.column_count

        for pattern in self._patterns:
            if board.check_line_horizontal(x_min, x_max, y_last, pattern):
                return True, pattern[0]

        return False, None

    def _has_winner_vertical(self, board, x_last):
        y_min = 0
        y_max = self._board.row_count

        for pattern in self._patterns:
            if board.check_line_vertical(y_min, y_max, x_last, pattern):
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
        x_max = self._board.column_count - Gomoku._LINE_WIN_SIZE + 1
        y_max = self._board.row_count - Gomoku._LINE_WIN_SIZE + 1

        for x in range(0, x_max):
            for y in range(0, y_max):
                for pattern in self._patterns:
                    line = board.get_diag_down(x, y, Gomoku._LINE_WIN_SIZE)
                    if line == pattern:
                        return True, pattern[0]

        return False, None

    def _has_winner_diag_up(self, board):
        '''
        @brief '/'
        '''
        x_min = Gomoku._LINE_WIN_SIZE - 1
        x_max = self._board.column_count
        y_max = self._board.row_count - Gomoku._LINE_WIN_SIZE + 1

        for x in range(x_min, x_max):
            for y in range(0, y_max):
                for pattern in self._patterns:
                    if board.get_diag_up(x, y, Gomoku._LINE_WIN_SIZE) == pattern:
                        return True, pattern[0]

        return False, None
