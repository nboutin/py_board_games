#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tictactoe.tictactoe import TicTacToe
from view.ascii_view import ASCII_View

def main():
    
    game = TicTacToe()
    view = ASCII_View(game.get_grid())

    view.display()

if __name__ == "__main__":
    main()
