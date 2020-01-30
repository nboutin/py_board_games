#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import neat
import os
import numpy as np
import pickle
import sys
sys.path.append("..")
from game_base.player import Player
from game_base.board import Token
from ai.minmax_ab import Minmax_AB
from game.connect_four import ConnectFour


GENOME_PATHNAME = os.path.join('genome', '0130_cf_genome_win_1940_28_l2')


def main(config_file):

    # Load configuration.
    config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
                         neat.DefaultSpeciesSet, neat.DefaultStagnation,
                         config_file)
    # load the winner
    with open(GENOME_PATHNAME, 'rb') as f:
        c = pickle.load(f)

    net = neat.nn.RecurrentNetwork.create(c, config)

    p1 = Player("Neat_1", Token.A)
    p2 = Player("AI_2", Token.B, True)
    ai = Minmax_AB(p2, 2, False)
    game = ConnectFour(p1=p1, p2=p2)

    while not game.is_over:
        cp = game.current_player

        if cp == p1:
            inputs = game.flat
            output = net.activate(inputs)
            move = np.argmax(output)

            if not game.is_valid_move(move):
                break
        else:
            move = ai.compute(game)

        game.play(move)

    print("History:", game.history)
    print("Winner:", game.winner)


if __name__ == '__main__':
    import os
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, 'config')
    main(config_path)
