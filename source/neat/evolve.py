#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import neat
import multiprocessing as mp
import pickle
import os
# import visualize

import cProfile
import pstats
from pstats import SortKey

# CORE_COUNT = 2
CORE_COUNT = mp.cpu_count()

# CHECKPOINT = os.path.join('genome', 'cf_chkpt_12349')
CHECKPOINT = None

# make pop global to be use in evaluate function
pop = None

def run(config_file):

    print("Using ", CORE_COUNT, " core")

    if CHECKPOINT is not None:
        pop = neat.Checkpointer.restore_checkpoint(CHECKPOINT)
    else:
        # Load configuration.
        config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
                             neat.DefaultSpeciesSet, neat.DefaultStagnation,
                             config_file)
    
        # Create the populatoin, which is the top-level object for a NEAT run.
        pop = neat.Population(config)

    # Add a stdout reporter to show progress in the terminal.
    pop.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    pop.add_reporter(stats)
    pop.add_reporter(neat.Checkpointer(generation_interval=1000,
                                       time_interval_seconds=300,
                                       filename_prefix='cf_chkpt_'))

    # Run until a solution is found.
    winner = None
    if CORE_COUNT == 1:
        winner = pop.run(evaluate)
    else:
        pe = neat.ParallelEvaluator(CORE_COUNT, eval_genome)
        winner = pop.run(pe.evaluate)

#     pr = cProfile.Profile()
#     pr.enable()
#     winner = pop.run(evaluate, 10)
#     pr.disable()
#     ps = pstats.Stats(pr)
#     ps.strip_dirs()
#     ps.sort_stats('tottime')
#     ps.print_stats()

    # Save the genome winner.
    pathname = os.path.join('genome', 'cf_genome_win')
    print('Save best genome:', pathname)
    with open(pathname, 'wb') as f:
        pickle.dump(winner, f)
        
    # Generate checkpoint of pop when winner is found
#     neat.Checkpointer(filename_prefix='cf_chkpt_').save_checkpoint(
#         config, pop, neat.DefaultSpeciesSet, 'win')


#     visualize.plot_stats(stats, ylog=False, view=False, filename="fitness.svg")
#     visualize.draw_net(config, winner, view=False, filename="winner-net.gv")


def evaluate(genomes, config):
    for genome_id, genome in genomes:
        genome.fitness = eval_genome(genome, config)


def eval_genome(genome, config):
    net = neat.nn.RecurrentNetwork.create(genome, config)
    return simulate_B(net)


import sys
sys.path.append("..")
from game_base.player import Player, PlayerNeat, PlayerMinmax
from game_base.board import Token
# from ai.minmax_ab import Minmax_AB
from game.connect_four import ConnectFour


def simulate_A(net):
    '''
    @param net to evaluate
    @return fitness of net
    '''
    # 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28
    # 28 * 390 = 10920
    episode_count = 7
    level = 1
    fitness = 0
    scores = list()

    # Increase Opponent level after each win
    for i in range(episode_count):
        p1 = PlayerNeat("Neat_1", net)
        p2 = PlayerMinmax("Minmax_1", Token.B, level, True)
        game = ConnectFour(p1=p1, p2=p2)
        run_game(game, p1, p2)
        set_score(game, p1, p2)

        fitness += p1.score * level if p1.score >= 0 else p1.score
        if game.winner == p1:
            level += 1

    return fitness


def simulate_B(net):
    '''
    Play 10 round against minmax
    win:200, draw:100, loose:0, bad move:0
    '''
    episode_count = 20
    level = 2
    fitness = 0
    
    for _ in range (episode_count):
        p1 = PlayerNeat("Neat_1", net)
        p2 = PlayerMinmax("Minmax_1", Token.B, level, True)
        
        game = ConnectFour(p1=p1, p2=p2)
        run_game(game)
        set_score(game, p1, p2, episode_count)
        
        fitness += p1.score
    return fitness

def run_game(game):
    while not game.is_over:
        move = game.current_player.next_move(game)
        if not game.is_valid_move(move):
            break
        game.play(move)

def set_score(game, p1, p2, n):
    '''
    @details Fitness is constructed as follow:
    - win game 200 (minus move count)
    - draw game 100
    - loose game 0 (plus move count)
    - invalid move, return move count
    '''

    move_count = game.moveCount / 2
    move_max = 6*7/2
    win_point = (move_max * n) * 2 - move_count
    draw_point = win_point / 2
    loose_point = 0 + move_count
    bad_move_point = 0

    if game.is_over:
        if game.winner == p1:
            p1.score = win_point
            p2.score = loose_point
        elif game.winner == p2:
            p1.score = loose_point
            p2.score = win_point
        else:  # draw
            p1.score = draw_point
            p2.score = draw_point
    else:  # bad move
        if game.current_player == p1:
            p1.score = bad_move_point
            p2.score = None # Opponent play invalid move
        else:
            p1.score = None # Opponent play invalid move
            p2.score = bad_move_point

if __name__ == "__main__":
    import os
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, 'config')
    run(config_path)
