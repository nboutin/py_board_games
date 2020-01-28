#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import neat
import multiprocessing as mp
# import visualize

CORE_COUNT = mp.cpu_count()
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
    return simulate(net, config)


def simulate(net, config):
    ''' return: fitness

        Actions consist of 3 sub-actions:
        - Direction to move the read head (left or right, plus up and down for 2-d envs)
        - Whether to write to the output tape
        - Which character to write (ignored if the above sub-action is 0)

        Reward schedule:
            write a correct character: +1
            write a wrong character: -.5
            run out the clock: -1
            otherwise: 0
    '''
    return 0
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
    