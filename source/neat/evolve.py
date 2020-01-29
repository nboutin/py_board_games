#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import neat
import multiprocessing as mp
# import visualize

CORE_COUNT = 1  # mp.cpu_count()
EPISODE_COUNT = 100


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
#     p.add_reporter(neat.Checkpointer(5))

    # Run until a solution is found.
    winner = None
    if CORE_COUNT == 1:
        winner = p.run(evaluate)
    else:
        pe = neat.ParallelEvaluator(CORE_COUNT, eval_genome)
        winner = p.run(pe.evaluate)

    # Display the winning genome.
    print('\nBest genome:\n{!s}'.format(winner))

#     visualize.plot_stats(stats, ylog=False, view=False, filename="fitness.svg")

    name = 'winner'
    g = winner
#     visualize.draw_net(config, g, view=False, filename=name + "-net.gv")

    # Execute Winner
#     net = neat.nn.RecurrentNetwork.create(winner, config)
#     env = gym.make('Copy-v0')
#     env = wrappers.Monitor(env, directory="monitor", force=True)
# #     env = wrappers.Monitor(env, directory="monitor", video_callable=lambda eid: True, force=True)
#
#     for i in range(EPISODE_COUNT):
#         observation = env.reset()
#         net.reset()
#         while True:
#             env.render()
#             inputs = [0] * int(env.observation_space.n)
#             inputs[observation] = 1
#             output = net.activate(inputs)
#
#             d = output[0:2]
#             w = output[2:4]
#             c = output[4:]
#             action = (np.argmax(d), np.argmax(w), np.argmax(c))
#             observation, reward, done, info = env.step(action)
#
#             if done:
#                 break
#     env.close()


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
    - win game +1000 (minus move count)
    - loose game 100 (plus move count)
    - draw game 500
    - invalid move, return move count
    - accumulate points over 5 matches
    - Max Fitness = 5 * (1000 - 4) = 4800
    @todo
    - How to balance loose game and invalid move
    - increase AI level after a win

    numpy.argmax: Returns the indices of the maximum values along an axis.
    '''
    episode_count = 5
    move_count_max = 6 * 7 / 2  # 21
    win_point = move_count_max * episode_count
    draw_point = win_point / 2
    loose_point = 0
    fitness = 0

    for i in range(episode_count):
        p1 = Player("Neat_1", Token.A)
        p2 = Player("AI_2", Token.B, True)
        ai = Minmax_AB(p2, 2)
        game = ConnectFour(p1=p1, p2=p2)
        bbx = game.bitboard[0]
        bbo = game.bitboard[1]

        move_count = 0

        while not game.is_over:
            cp = game.current_player

            # Convert game board to inputs matrix
            inputs = list()
            for i in range(5, -1, -1):
                for j in range(0 + i, 47 + i, 7):
                    if (bbx >> j) & 1:
                        inputs.append(1)
                    elif (bbo >> j) & 1:
                        inputs.append(-1)
                    else:
                        inputs.append(0)

            if cp == p1:
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

    return fitness / episode_count

# def simulate(net, config):
#     ''' return: fitness
#
#         Actions consist of 3 sub-actions:
#         - Direction to move the read head (left or right, plus up and down for 2-d envs)
#         - Whether to write to the output tape
#         - Which character to write (ignored if the above sub-action is 0)
#
#         Reward schedule:
#             write a correct character: +1
#             write a wrong character: -.5
#             run out the clock: -1
#             otherwise: 0
#     '''
#     return 0
#     env = gym.make('Copy-v0')
#     fitness = 0
#
#     for i in range(EPISODE_COUNT):
#         observation = env.reset()
#         net.reset()
#         while True:
#             inputs = [0] * int(env.observation_space.n)
#             inputs[observation] = 1
#             output = net.activate(inputs)
#
#             d = output[0:2]
#             w = output[2:4]
#             c = output[4:]
#             action = (np.argmax(d), np.argmax(w), np.argmax(c))
#             observation, reward, done, info = env.step(action)
#
#             if done:
#                 fitness += reward
#                 break
#     env.close()
#     return fitness


if __name__ == "__main__":
    import os
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, 'config')
    run(config_path)
