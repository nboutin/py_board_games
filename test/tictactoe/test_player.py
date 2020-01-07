#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
import sys
import os
sys.path.insert(0, os.path.join(sys.path[0], 'source'))

from tictactoe.player import Player
from tictactoe.board import Token


class TestPlayer(unittest.TestCase):

    def test_name(self):
        name = "Player 1"
        token = Token.CROSS
        player = Player(name, token)
        self.assertEqual(player.name, name)
        self.assertEqual(player.token, token)


if __name__ == '__main__':
    unittest.main()
