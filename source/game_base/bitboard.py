#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class BitBoard():
    '''
    Based on https://github.com/denkspuren/BitboardC4/blob/master/BitboardDesign.md

     6 13 20 27 34 41 48   55 62     Additional row
    +---------------------+ 
    | 5 12 19 26 33 40 47 | 54 61     top row
    | 4 11 18 25 32 39 46 | 53 60
    | 3 10 17 24 31 38 45 | 52 59
    | 2  9 16 23 30 37 44 | 51 58
    | 1  8 15 22 29 36 43 | 50 57
    | 0  7 14 21 28 35 42 | 49 56 63  bottom row
    +---------------------+
    '''

    def __init__(self):
        '''
        '''
        # Index 0 for 'x', Index 1 for 'o'
        self._bitboard = [0, 0]
        # Serves as a memory where the next token goes given the column
        self._height = [0, 7, 15, 24, 30, 35, 42]
        # Number of moves done
        self._counter = 0
        # Remember the moves done so far
        self._moves = list()

    def makeMove(self, col):
        '''
        @param col ranging from 0 to 6
        '''
        move = 1 << self._height[col]
        self._height[col] += 1
        self._bitboard[self._counter & 1] ^= move
        self._moves.append(col)
        self._counter += 1

    def undoMove(self):
        self._counter -= 1
        col = self._moves[self._counter]
        self._height[col] -= 1
        move = 1 << self._height[col]
        self._bitboard[self._counter & 1] ^= move

    def isWin(self):
        '''
        @brief Check whether there are four in row
        '''
        pass

    def listMoves(self):
        '''
        @brief List all possible moves in a given situation
        '''
        pass

    def __str__(self):
        s = ''
        for bb in self._bitboard:
            s += '{:064b}\n'.format(bb)
        return s
