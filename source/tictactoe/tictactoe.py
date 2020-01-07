#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tictactoe.board import (Token, Board, Point)
from tictactoe.player import Player


class TicTacToe():

    def __init__(self, p1=None, p2=None):
        self._board = Board()
        self._p1 = p1 if not p1 is None else Player("Player 1", Token.CROSS)
        self._p2 = p2 if not p2 is None else Player("Player 2", Token.CIRCLE)
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

    def play(self, point):
        if self._is_over:
            self._moves.append(None)    # bad move
            return False

        if not self._board.play(point, self._current_player.token):
            self._moves.append(None)    # bad move
            return False

        self._moves.append(point)
        self._compute_ending()
        self._compute_next_player()

        return True

    def undo(self):
        move = self._moves.pop()
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
        if self._board.played_cell_count < 5:
            return False

        # Horizontal
        has_winner, token = self._has_winner_horizontal(self._board.grid)

        # Vertical
        if not has_winner:
            has_winner, token = self._has_winner_vertical(self._board.grid)

        # Diagonal
        if not has_winner:
            has_winner, token = self._has_winner_diagonal(self._board.grid)

        if has_winner:
            self._winner_player = self._p1 if token == self._p1.token else self._p2

        self._is_over = not self._board.has_free_cell() or has_winner
        return self._is_over

    def _has_winner_horizontal(self, grid):

        for token in [Token.CROSS, Token.CIRCLE]:
            test_line = [token for x in range(3)]

            for row in grid:
                if row == test_line:
                    return True, token

        return False, None

    def _has_winner_vertical(self, grid):
        grid_rotated = self._rotate(self._board.grid)
        return self._has_winner_horizontal(grid_rotated)

    def _rotate(self, grid):
        return list(list(a) for a in zip(*reversed(grid)))

    def _has_winner_diagonal(self, grid):

        if not grid[0][0] is None and grid[0][0] == grid[1][1] and grid[0][0] == grid[2][2]:
            return True, grid[0][0]

        if not grid[0][2] is None and grid[0][2] == grid[1][1] and grid[0][2] == grid[2][0]:
            return True, grid[0][2]

        return False, None
