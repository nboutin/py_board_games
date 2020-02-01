#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import numpy as np

sys.path.append("..")
from ai.minmax_ab import Minmax_AB


class Player():

    def __init__(self, name):
        self._name = name
        self._turn = None
        self.score = 0

    @property
    def name(self):
        return self._name
    
    @property
    def turn(self):
        return self._turn
    
    @turn.setter
    def turn(self, t):
        self._turn = t

    def next_move(self, game):
        raise Exception("Not implemented")

    def __str__(self):
        return self._name + '(' + self._turn + ')'

class PlayerHuman(Player):
    
    def __init__(self, name):
        super().__init__(name)
        
    def next_move(self, game):
        return int(input("Enter (x): "))

class PlayerMinmax(Player):

    def __init__(self, name, level, rand=False):
        super().__init__(name)
        self._ai = Minmax_AB(self, level, rand)

    def next_move(self, game):
        return self._ai.compute(game)


class PlayerNeat(Player):

    def __init__(self, name, net):
        super().__init__(name)
        self._net = net

    def next_move(self, game):
        '''numpy.argmax: Returns the indices of the maximum scores along an axis.'''
        return np.argmax(self._net.activate(game.flat))
