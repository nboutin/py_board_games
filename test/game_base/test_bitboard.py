#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os
sys.path.insert(0, os.path.join(sys.path[0], 'source'))

import unittest
from game_base.bitboard import BitBoard


class TestBoard(unittest.TestCase):

    def test_init(self):
        bb = BitBoard()

    def test_makeMove(self):
        bb = BitBoard()
        bb.makeMove(0)
        bb.makeMove(1)

        print(bb)

    def test_undoMove(self):
        bb = BitBoard()
        bb.makeMove(0)
        bb.makeMove(1)
        bb.undoMove()
        print(bb)
