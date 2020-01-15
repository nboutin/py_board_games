#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
import sys
import os
sys.path.insert(0, os.path.join(sys.path[0], 'source'))

from game_base.board import Point


class TestPoint(unittest.TestCase):

    def test_init(self):
        p = Point()

    def test_compare(self):

        self.assertEqual(Point(1, 2), Point(1, 2))
        self.assertNotEqual(Point(3, 2), Point(1, 2))

    def test_hash(self):

        l = [Point(3, 2), Point(1, 2), Point(0, 2), Point(2, 1)]
        set(l)
