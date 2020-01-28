#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from game_base.board import Token


class ASCII_View():

    def __init__(self, grid=None, bitboard=None):
        self._grid = grid
        self._bitboard = bitboard
        self._messages = list()
        self.current_player = None
        self._history = list()

    def welcome(self, title, version):
        print('{} {}'.format(title, version))

    def display(self):
        self._print_messages()
        print('-----')
        if self._grid is not None:
            self._print_grid(self._grid)
        else:
            self._print_bitboard(self._bitboard)
        self._print_history()
        self._print_player(self.current_player)

    def ask_input(self, n):
        if n == 1:
            i = input("Enter (x): ")
            return int(i)
        else:
            i = input("Enter (x,y): ")
            return int(i[0]), int(i[1])

    def add_message(self, msg):
        self._messages.append(msg)

    def set_history(self, h):
        self._history = h

    def _print_grid(self, grid):

        print('  ', end='')
        for i in range(len(grid[0])):
            print('{} '.format(i), end='')
        print()

        for i, row in enumerate(grid):
            print('{}|'.format(i), end='')
            for cell in row:
                print(self._token_str(cell) + "|", end='')
            print('')

    def _print_bitboard(self, bitboard):
        s = '\n'
        bbx = bitboard[0]
        bbo = bitboard[1]

        for i in range(7):
            s += str(i) + ' '
        s += '\n'

        for i in range(5, -1, -1):
            for j in range(0 + i, 47 + i, 7):
                if (bbx >> j) & 1:
                    s += 'x|'
                elif (bbo >> j) & 1:
                    s += 'o|'
                else:
                    s += '-|'
            s += '\n'
        print(s)

    def _print_player(self, player):
        print(player.name + '(' + self._token_str(player.token) + ')')

    def _token_str(self, token):
        if token is None:
            return '-'
        elif token in [Token.A]:
            return 'X'
        elif token in [Token.B]:
            return 'O'
        else:
            assert False

    def _print_messages(self):
        for msg in self._messages:
            print(msg)

        self._messages.clear()

    def _print_history(self):
        if self._history:
            print('History:', end='')
            for m in self._history:
                print('{},'.format(m), end='')
            print()
