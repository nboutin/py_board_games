#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os
sys.path.insert(0, os.path.join(sys.path[0], 'source'))

import unittest
from game_base.bitboard import BitBoard


class TestBoard(unittest.TestCase):

    def test_init(self):
        board = BitBoard()
        bb = board._bitboard
        self.assertEqual(bb[0], 0)
        self.assertEqual(bb[1], 0)

    def test_makeMove(self):
        board = BitBoard()
        bb = board._bitboard

        board.makeMove(0)
        x = 1
        o = 0
        self.assertEqual(bb[0], x)
        self.assertEqual(bb[1], o)

        board.makeMove(1)
        o |= 1 << 7
        board.makeMove(1)
        x |= 1 << 8
        self.assertEqual(bb[0], x)
        self.assertEqual(bb[1], o)

        board.makeMove(2)
        o |= 1 << 14
        board.makeMove(2)
        x |= 1 << 15
        board.makeMove(2)
        o |= 1 << 16
        self.assertEqual(bb[0], x)
        self.assertEqual(bb[1], o)

    def test_col_6(self):
        board = BitBoard()
        bb = board._bitboard

        board.makeMove(6)
        board.makeMove(6)
        x = 1 << 42
        o = 1 << 43
        self.assertEqual(bb[0], x)
        self.assertEqual(bb[1], o)

        board.makeMove(5)
        board.makeMove(5)
        x |= 1 << 35
        o |= 1 << 36
        self.assertEqual(bb[0], x)
        self.assertEqual(bb[1], o)

        board.makeMove(4)
        board.makeMove(4)
        x |= 1 << 28
        o |= 1 << 29
        self.assertEqual(bb[0], x)
        self.assertEqual(bb[1], o)

    def test_undoMove(self):
        board = BitBoard()
        bb = board._bitboard

        # one move
        board.makeMove(0)
        self.assertEqual(bb[0], 1)
        self.assertEqual(board.currentPlayer, 1)

        board.undoMove()
        self.assertEqual(bb[0], 0)
        self.assertEqual(board.currentPlayer, 0)

        # first column
        board.makeMove(0)
        board.makeMove(0)
        board.makeMove(0)
        board.makeMove(0)
        x = 1 | 1 << 2
        o = 1 << 1 | 1 << 3
        self.assertEqual(bb[0], x)
        self.assertEqual(bb[1], o)
        self.assertEqual(board.currentPlayer, 0)

        board.undoMove()
        o ^= 1 << 3
        self.assertEqual(bb[0], x)
        self.assertEqual(bb[1], o)
        self.assertEqual(board.currentPlayer, 1)

        board.undoMove()
        x ^= 1 << 2
        self.assertEqual(bb[0], x)
        self.assertEqual(bb[1], o)
        self.assertEqual(board.currentPlayer, 0)

        # horizontal
        board = BitBoard()
        bb = board._bitboard
        board.makeMove(0)
        board.makeMove(1)
        board.makeMove(2)
        board.makeMove(3)
        x = 1 | 1 << 14
        o = 1 << 7 | 1 << 21
        self.assertEqual(bb[0], x)
        self.assertEqual(bb[1], o)
        self.assertEqual(board.currentPlayer, 0)
        
        board.undoMove()
        o ^= 1 << 21
        self.assertEqual(bb[0], x)
        self.assertEqual(bb[1], o)
        self.assertEqual(board.currentPlayer, 1)

        board.undoMove()
        x ^= 1 << 14
        self.assertEqual(bb[0], x)
        self.assertEqual(bb[1], o)
        self.assertEqual(board.currentPlayer, 0)

    def test_isWin(self):
        bb = BitBoard()
        self.assertFalse(bb.isWin(0))
        self.assertFalse(bb.isWin(1))

    def test_listMoves(self):
        board = BitBoard()

        self.assertEqual(board.listMoves(), [0, 1, 2, 3, 4, 5, 6])
        for i in range(6):
            board.makeMove(0)
        self.assertEqual(board.listMoves(), [1, 2, 3, 4, 5, 6])

        for i in range(6):
            board.makeMove(6)
        self.assertEqual(board.listMoves(), [1, 2, 3, 4, 5])

        for i in range(6):
            board.makeMove(3)
        self.assertEqual(board.listMoves(), [1, 2, 4, 5])

    def test_seqA(self):
        board = BitBoard()
        moves = [6, 6, 5, 5, 4, 4, 3]
        for m in moves:
            board.makeMove(m)

        self.assertTrue(board.isWin(0))
