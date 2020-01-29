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


CHECKPOINT_FILENAME = os.path.join('best', '0129_cf_chkpt_win_10500')


def main(config_file):

    # Load configuration.
    config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
                         neat.DefaultSpeciesSet, neat.DefaultStagnation,
                         config_file)
    # load the winner
    with open('winner-ctrnn', 'rb') as f:
        c = pickle.load(f)

    net = neat.nn.RecurrentNetwork.create(c, config)


    p1 = Player("Neat_1", Token.A)
    p2 = Player("AI_2", Token.B, True)
    ai = Minmax_AB(p2, 2)
    game = ConnectFour(p1=p1, p2=p2)

    while not game.is_over:
        cp = game.current_player

        # Convert game board to inputs matrix
        inputs = bitboardToMatrix(game.bitboard)

        if cp == p1:
            output = net.activate(inputs)
            move = np.argmax(output)

            if not game.is_valid_move(move):
                break
        else:
            move = ai.compute(game)

        game.play(move)

    output = net.activate(inputs)
    move = np.argmax(output)

def bitboardToMatrix(bb):
    bbx = bb[0]
    bbo = bb[1]

    inputs = list()
    for i in range(5, -1, -1):
        for j in range(0 + i, 47 + i, 7):
            if (bbx >> j) & 1:
                inputs.append(1)
            elif (bbo >> j) & 1:
                inputs.append(-1)
            else:
                inputs.append(0)
    return inputs

if __name__ == '__main__':
    import os
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, 'config')
    main(config_path)
