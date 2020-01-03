#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from tictactoe.board import Token


class ASCII_View():

    def __init__(self, grid):
        self._grid = grid

    def display(self):
        self._print_grid(self._grid)

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
