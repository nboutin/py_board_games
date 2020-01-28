#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from game_base.player import Player
from game_base.board import Token, Point
from game_base.ascii_view import ASCII_View
from game.tictactoe import TicTacToe
from game.connect_four import ConnectFour
from game.gomoku import Gomoku
from ai.minmax_ab_parallel import Minmax_AB_Parallel
from ai.minmax_ab import Minmax_AB

VERSION = "1.4.0-dev"


def main(game_name, player_mode, level):

    if not game_name or not player_mode or not level:
        game_name = menu_list(
            'Select game', ['TicTacToe', 'Connect Four', 'Gomoku'], 0)
        player_mode = menu_list('Select player mode', [
                                'H_H', 'AI_H', 'H_AI', 'AI_AI'], 3)
        level = select_level(game_name) if not (player_mode == 'H_H') else None

    print('{} {} {}'.format(game_name, player_mode, level))

    p1, p2 = make_player(player_mode)
    ai1, ai2 = make_ai(player_mode, level, p1, p2)
    game = make_game(game_name, p1, p2)

    view = make_view(game_name, game)
    view.welcome(game_name, VERSION)

    while game.is_over == False:
        view.current_player = game.current_player
        view.display()

        if game.current_player.is_ai:
            ai = ai1 if game.current_player == p1 else ai2
            move = ai.compute(game)
            view.add_message("Move: {} ({}s)".format(
                move, ai.computation_time))
        else:
            if game_name == "Connect Four":
                move = view.ask_input(1)
            else:
                x, y = view.ask_input(2)
                move = Point(x, y)

        if not game.is_valid_move(move):
            view.add_message("Input is invalid")
        else:
            game.play(move)

    # End of Game
    if game.winner is None:
        view.add_message("Game is finished. Draw")
    else:
        view.add_message("Game is finished")
        view.add_message("Winner is {}".format(game.winner.name))
    view.display()


def menu_list(title, items, default):
    print('{} ({}):'.format(title, default))
    for n, i in enumerate(items):
        print('  {} {}'.format(n, i))
    choice = input('Choice:')
    if not choice:
        choice = default
        print(choice)
    print()
    return items[int(choice)]


def select_level(game_name):
    game_level_default = {'TicTacToe': 9, 'Connect Four': 11, 'Gomoku': 4}
    level_default = game_level_default[game_name]
    level = input('Level ({}):'.format(level_default))
    print()
    return int(level) if level else level_default


def make_player(mode):

    p1, p2 = None, None

    if mode == 'H_H':
        p1 = Player("Human_1", Token.A)
        p2 = Player("Human_2", Token.B)
    elif mode == 'AI_H':
        p1 = Player("AI_1", Token.A, True)
        p2 = Player("Human_2", Token.B)
    elif mode == 'H_AI':
        p1 = Player("Human_1", Token.A)
        p2 = Player("AI_2", Token.B, True)
    elif mode == 'AI_AI':
        p1 = Player("AI_1", Token.A, True)
        p2 = Player("AI_2", Token.B, True)
    else:
        assert(False)

    return p1, p2


def make_ai(mode, level, p1, p2):

    ai1, ai2 = None, None
    if mode == 'AI_H':
        ai1 = Minmax_AB(p1, level)
    elif mode == 'H_AI':
        ai2 = Minmax_AB(p2, level)
    elif mode == 'AI_AI':
        ai1 = Minmax_AB(p1, level)
        ai2 = Minmax_AB(p2, level)

    return ai1, ai2


def make_game(game_name, p1, p2):

    game = None
    if game_name == 'TicTacToe':
        game = TicTacToe(p1=p1, p2=p2)
    elif game_name == 'Connect Four':
        game = ConnectFour(p1=p1, p2=p2)
    elif game_name == 'Gomoku':
        game = Gomoku(p1=p1, p2=p2)
    else:
        assert(False)
    return game


def make_view(game_name, game):

    if game_name == 'Connect Four':
        return ASCII_View(bitboard=game.bitboard)
    else:
        return ASCII_View(grid=game.grid)


if __name__ == "__main__":
    import sys

    game_name, player_mode, level = None, None, None
    if len(sys.argv) == 4:
        game_name = sys.argv[1]
        player_mode = sys.argv[2]
        level = sys.argv[3]
    main(game_name, player_mode, level)
