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
        #         self._board = BoardDrop(ConnectFour._COLUMN, ConnectFour._ROW)
        self._board = BitBoard()
        self._p1 = p1 if not p1 is None else Player("Player 1", Token.A)
        self._p2 = p2 if not p2 is None else Player("Player 2", Token.B)
#         self._current_player = self._p1
        self._winner_player = None
        self._is_over = False
#         self._history = list()
        self._moves = [i for i in range(ConnectFour._COLUMN)]
#         self._patterns = [np.full(4, token) for token in [Token.A, Token.B]]

    @property
    def bitboard(self):
        return self._board._bitboard

    @property
    def is_over(self):
        return self._is_over

    @property
    def current_player(self):
        #         return self._current_player
        return self._p1 if self._board.currentPlayer == 0 else self._p2

    @property
    def winner(self):
        return self._winner_player

    @property
    def history(self):
        #         return self._history
        return self._board._moves

    def generate_moves(self):
        '''
        @brief All legal moves
        @details Removing move from full column does not improve performances
        '''
        return self._board.listMoves()

    def play(self, move):
        if self._is_over:
            #             self._history.append(None)    # bad move
            return False

        current_player = self._board.currentPlayer
        self._board.makeMove(move)

#         if not self._board.drop_token(move, self._current_player.token):
#             self._history.append(None)    # bad move
#             return False

#         self._history.append(move)
        self._compute_ending(current_player)
#         self._compute_next_player()

        return True

    def undo(self):
        #         move = self._history.pop()
        #         if move is not None:
        #             self._board.undo(move)
        #             self._compute_next_player()

        self._board.undoMove()
        self._winner_player = None
        self._is_over = False

#     def _compute_next_player(self):
#         if self._current_player == self._p1:
#             self._current_player = self._p2
#         elif self._current_player == self._p2:
#             self._current_player = self._p1
#         else:
#             assert False

    def _compute_ending(self, current_player):
        '''
        Decide if a game is over
        '''

# if self._board.cell_used_count < (ConnectFour._LINE_WIN_SIZE * 2) - 1:
        if self._board._counter < (ConnectFour._LINE_WIN_SIZE * 2) - 1:
            return False

#         # Horizontal
#         has_winner, token = self._has_winner_horizontal(
#             self._board, self._board.last_move)
#
#         # Vertical
#         if not has_winner:
#             has_winner, token = self._has_winner_vertical(
#                 self._board, self._board.last_move)
#
#         # Diagonal
#         if not has_winner:
#             has_winner, token = self._has_winner_diagonal(
#                 self._board, self._board.last_move)

        has_winner = self._board.isWin(current_player)

        if has_winner:
            #             self._winner_player = self._p1 if token == self._p1.token else self._p2
            self._winner_player = self._p1 if current_player == 0 else self._p2

        self._is_over = not self._board.hasFreeCell() or has_winner
        return self._is_over

#     def _has_winner_horizontal(self, board, move):
#         x, y = move.point
#         for pattern in self._patterns:
#             if board.check_line_horizontal(x, y, pattern):
#                 return True, pattern[0]
#
#         return False, None
#
#     def _has_winner_vertical(self, board, move):
#         x, y = move.point
#         for pattern in self._patterns:
#             if board.check_line_vertical(x, y, pattern):
#                 return True, pattern[0]
#
#         return False, None
#
#     def _has_winner_diagonal(self, board, move):
#         x, y = move.point
#         for pattern in self._patterns:
#             if board.check_line_diag_down(x, y, pattern):
#                 return True, pattern[0]
#             elif board.check_line_diag_up(x, y, pattern):
#                 return True, pattern[0]
#         return False, None
