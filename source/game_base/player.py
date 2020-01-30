#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
sys.path.append("..")
from ai.minmax_ab import Minmax_AB
import numpy as np


class Player():

    def __init__(self, name, token, is_ai=False):
        self._name = name
        self._token = token
        self._is_ai = is_ai
        self.score = 0

    @property
    def name(self):
        return self._name

    @property
    def token(self):
        return self._token

    @property
    def is_ai(self):
        return self._is_ai

    @is_ai.setter
    def is_ai(self, val):
        self._is_ai = val

    def __str__(self):
        return self._name


class PlayerMinmax(Player):

    def __init__(self, name, token, level, rand=False):
        super().__init__(name, token, True)
        self._ai = Minmax_AB(self, level, rand)

    def next_move(self, game):
        return self._ai.compute(game)


class PlayerNeat(Player):

    def __init__(self, name, net):
        super().__init__(name, None, True)
        self._net = net

    def next_move(self, game):
        '''numpy.argmax: Returns the indices of the maximum scores along an axis.'''
        return np.argmax(self._net.activate(game.flat))
