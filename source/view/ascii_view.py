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
        print('-----')
        self._print_grid(self._grid)
        self._print_player(self.current_player)
        self._print_messages()

    def ask_input(self):
        i = input("Enter (x,y): ")
        return int(i[0]), int(i[1])

    def message(self, msg):
        self._messages.append(msg)

    def _print_grid(self, grid):
        print ('  0 1 2')
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
        elif token == Token.CROSS:
            return 'X'
        elif token == Token.CIRCLE:
            return 'O'
        else:
            assert False

    def _print_messages(self):
        for msg in self._messages:
            print(msg)

        self._messages.clear()
