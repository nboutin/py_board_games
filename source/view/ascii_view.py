#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from tictactoe.board import Token


class ASCII_View():

    def __init__(self, grid):
        self._grid = grid
        self._messages = list()

    def display(self):
        self._print_grid(self._grid)
        self._print_messages()

    def ask_input(self):
        i = input("Enter index [0-8]: ")
        i = int(i)
        return int(i / 3), i % 3
    
    def message(self, msg):
        self._messages.append(msg)

    def _print_grid(self, grid):
        for row in grid:
            for cell in row:
                self._print_cell(cell)
            print('')

    def _print_cell(self, cell):

        if cell is None:
            print('-', end='')
        elif cell == Token.CROSS:
            print('X', end='')
        elif cell == Token.CIRCLE:
            print('O', end='')
            
    def _print_messages(self):
        for msg in self._messages:
            print(msg)
