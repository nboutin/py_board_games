#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from tictactoe.board import Token


class ASCII_View():

    def __init__(self, grid):
        self._grid = grid
        self._messages = list()
        self.current_player = None

    def welcome(self, title, version):
        print('{} {}'.format(title, version))

    def display(self):
        self._print_messages()
        print('-----')
        self._print_grid(self._grid)
        self._print_player(self.current_player)

    def ask_input(self):
        i = input("Enter (x,y): ")
        return int(i[0]), int(i[1])

    def message(self, msg):
        self._messages.append(msg)

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

    def _print_player(self, player):
        print(player.name + '(' + self._token_str(player.token) + ')')

    def _token_str(self, token):
        if token is None:
            return '-'
        elif token in [Token.CROSS]:
            return 'X'
        elif token in [Token.CIRCLE]:
            return 'O'
        else:
            assert False

    def _print_messages(self):
        for msg in self._messages:
            print(msg)

        self._messages.clear()
