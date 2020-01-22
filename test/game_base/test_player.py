#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
import copy
import sys
import os
sys.path.insert(0, os.path.join(sys.path[0], 'source'))

from game_base.player import Player


class TestPlayer(unittest.TestCase):

    def test_name(self):
        name = "Player 1"
        token = "X"
        player = Player(name, token)
        self.assertEqual(player.name, name)
        self.assertEqual(player.token, token)

    def test_deepcopy(self):
        name = "Player 1"
        token = "X"
        p = Player(name, token)
        pp = p
        cp = copy.deepcopy(p)

        self.assertEqual(p.name, cp.name)
        self.assertEqual(p.token, cp.token)
        self.assertTrue(isinstance(cp, Player))
        self.assertFalse(p is cp)
        self.assertTrue(p is pp)

        # Update attributes values so 'is' return False
        p._name = "Human"
        p._token = 'o'

        self.assertFalse(p.name is cp.name)
        self.assertFalse(p.token is cp.token)


if __name__ == '__main__':
    unittest.main()
