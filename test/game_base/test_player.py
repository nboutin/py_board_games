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
        player = Player(name)
        self.assertEqual(player.name, name)

    def test_deepcopy(self):
        name = "Player 1"
        p = Player(name)
        pp = p
        cp = copy.deepcopy(p)

        self.assertEqual(p.name, cp.name)
        self.assertTrue(isinstance(cp, Player))
        self.assertFalse(p is cp)
        self.assertTrue(p is pp)

        # Update attributes values so 'is' return False
        p._name = "Human"

        self.assertFalse(p.name is cp.name)


if __name__ == '__main__':
    unittest.main()
