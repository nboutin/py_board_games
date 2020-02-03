#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import neat
import os
import numpy as np
import pickle
import sys
sys.path.append("..")
from game_base.player import PlayerNeat, PlayerMinmax
from game_base.board import Token
from ai.minmax_ab import Minmax_AB
from game.connect_four import ConnectFour


# GENOME_PATHNAME = os.path.join('genome', '0130_cf_genome_win_1940_28_l2')
# GENOME_PATHNAME = os.path.join('genome', '0130_cf_genome_win_5895_11')
# GENOME_PATHNAME = os.path.join('genome', '0202_cf_genome_win')
GENOME_PATHNAME = os.path.join('genome', 'cf_genome_win')


def main(config_file):

    # Load configuration.
    config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
                         neat.DefaultSpeciesSet, neat.DefaultStagnation,
                         config_file)
    # load the winner
    with open(GENOME_PATHNAME, 'rb') as f:
        c = pickle.load(f)

    net = neat.nn.RecurrentNetwork.create(c, config)
    level = 2

    p1 = PlayerNeat("Neat_1", net)
    p2 = PlayerMinmax("Minmax_1", Token.B, level, True)
    game = ConnectFour(p1=p1, p2=p2)
    move = None

    while not game.is_over:
        move = game.current_player.next_move(game)
        if not game.is_valid_move(move):
            break
        game.play(move)

    print("Winner:", game.winner)
    print("History:", game.history)
    print("Current player:", game.current_player)
    print('Last move:', move)
    print(game._board)


if __name__ == '__main__':
    import os
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, 'config')
    main(config_path)
