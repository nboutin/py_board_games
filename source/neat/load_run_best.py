#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import neat

CHECKPOINT_FILENAME = ""


def main(config):

    p = neat.Checkpointer.restore_checkpoint(CHECKPOINT_FILENAME)
    net = neat.nn.RecurrentNetwork.create(p.best_genome, config)

    output = net.activate(inputs)
    move = np.argmax(output)

if __name__ == '__main__':
    import os
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, 'config')
    main(config_path)
