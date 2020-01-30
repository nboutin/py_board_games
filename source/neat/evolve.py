#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import neat
import multiprocessing as mp
import pickle
# import visualize

import cProfile
import pstats
from pstats import SortKey

# CORE_COUNT = 1
CORE_COUNT = mp.cpu_count() - 1


def run(config_file):

    print("Using ", CORE_COUNT, " core")

    # Load configuration.
    config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
                         neat.DefaultSpeciesSet, neat.DefaultStagnation,
                         config_file)

    # Create the population, which is the top-level object for a NEAT run.
    p = neat.Population(config)

    # Add a stdout reporter to show progress in the terminal.
    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)
    p.add_reporter(neat.Checkpointer(generation_interval=1000,
                                     time_interval_seconds=300,
                                     filename_prefix='cf_chkpt_'))

    # Run until a solution is found.
    winner = None
    if CORE_COUNT == 1:
        winner = p.run(evaluate)
    else:
        pe = neat.ParallelEvaluator(CORE_COUNT, eval_genome)
        winner = p.run(pe.evaluate)

#     pr = cProfile.Profile()
#     pr.enable()
#     winner = p.run(evaluate, 100)
#     pr.disable()
#     ps = pstats.Stats(pr)
#     ps.strip_dirs()
#     ps.sort_stats('tottime')
#     ps.print_stats()

    # Display the winning genome.
#     print('\nBest genome:\n{!s}'.format(winner))
#     print('\nBest genome:\n{!s}'.format(p.best_genome))

    # Generate checkpoint of population when winner is found
    neat.Checkpointer(filename_prefix='cf_chkpt_').save_checkpoint(
        config, p, neat.DefaultSpeciesSet, 'win')

    # Save the genome winner.
    with open(os.path.join('genome', 'cf_genome_win'), 'wb') as f:
        pickle.dump(winner, f)

#     visualize.plot_stats(stats, ylog=False, view=False, filename="fitness.svg")
#     visualize.draw_net(config, winner, view=False, filename="winner-net.gv")


def evaluate(genomes, config):
    for genome_id, genome in genomes:
        genome.fitness = eval_genome(genome, config)


def eval_genome(genome, config):
    net = neat.nn.RecurrentNetwork.create(genome, config)
    return simulate(net)


import numpy as np
import sys
sys.path.append("..")
from game_base.player import Player
from game_base.board import Token
from ai.minmax_ab import Minmax_AB
from game.connect_four import ConnectFour


def simulate(net):
    '''
    @param net to evaluate
    @return fitness of net
    @details Fitness is constructed as follow:
    - win game +400 (minus move count)
    - loose game 0 (plus move count)
    - draw game 200
    - invalid move, return move count
    - accumulate points over 5 matches
    - Max Fitness = 5 * (400 - 4) ~= 2000
    @todo
    - increase AI level after a win

    numpy.argmax: Returns the indices of the maximum values along an axis.
    '''
    episode_count = 5
    move_count_max = 6 * 7 / 2  # 21
    draw_point = 200  # at least > 21*5*2
    win_point = draw_point * 2
    loose_point = 0
    fitness = 0

    for i in range(episode_count):
        p1 = Player("Neat_1", Token.A)
        p2 = Player("AI_2", Token.B, True)
        ai = Minmax_AB(p2, 6)
        game = ConnectFour(p1=p1, p2=p2)
        move_count = 0

        while not game.is_over:
            cp = game.current_player

            if cp == p1:
                inputs = game.flat
                output = net.activate(inputs)
                move = np.argmax(output)

                if not game.is_valid_move(move):
                    break
                else:
                    move_count += 1
            else:
                move = ai.compute(game)

            game.play(move)

        if game.is_over:
            if game.winner == p1:  # Neat win
                fitness += win_point - move_count
            elif game.winner == p2:  # Neat loose
                fitness += loose_point + move_count
            else:  # draw
                fitness += draw_point
        else:
            fitness += move_count

    return fitness


if __name__ == "__main__":
    import os
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, 'config')
    run(config_path)
