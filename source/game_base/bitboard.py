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
        self._height = [0, 7, 14, 21, 28, 35, 42]
        # Number of moves done
        self._counter = 0
        # Remember the moves done so far
        self._moves = list()
        # Token count for each column
        self._column_count = [6 for _ in range(7)]
        # Flat view to be use by Neural Network
        self._flat = [0 for _ in range(49)]

    @property
    def currentPlayer(self):
        '''
        @return 0 if player 1, 1 if player 2
        '''
        return self._counter & 1

    def hasFreeCell(self):
        return self._counter < (6 * 7)

    def makeMove(self, col):
        '''
        @param col ranging from 0 to 6
        void makeMove(int col)
            long move = 1L << height[col]++;
            bitboard[counter & 1] ^= move;  
            moves[counter++] = col;
        '''
        move = 1 << self._height[col]
        self._flat[self._height[col]] = -1 if self._counter & 1 else 1
        self._height[col] += 1
        self._bitboard[self._counter & 1] ^= move
        self._moves.append(col)
        self._counter += 1
        self._column_count[col] -= 1

    def undoMove(self):
        '''
        int col = moves[--counter];
        long move = 1L << --height[col];
        bitboard[counter & 1] ^= move;
        '''
        self._counter -= 1
        col = self._moves.pop()
        self._height[col] -= 1
        move = 1 << self._height[col]
        self._flat[self._height[col]] = 0
        self._bitboard[self._counter & 1] ^= move
        self._column_count[col] += 1

#     def isWin(self, player):
#         '''
#         @brief Check whether there are four in row
#         @param player index, 0 player 1, 1 player 2
#         '''
#         bb = self._bitboard[player]
#
#         # diagonal \
#         if (bb & (bb >> 6) & (bb >> 12) & (bb >> 18) != 0):
#             return True
#         # diagonal /
#         if (bb & (bb >> 8) & (bb >> 16) & (bb >> 24) != 0):
#             return True
#         # horizontal
#         if (bb & (bb >> 7) & (bb >> 14) & (bb >> 21) != 0):
#             return True
#         # vertical
#         if (bb & (bb >> 1) & (bb >> 2) & (bb >> 3) != 0):
#             return True
#         return False

    def isWin(self, player):
        '''
        boolean isWin(long bitboard) {
            int[] directions = {1, 7, 6, 8};
            long bb;
            for(int direction : directions) {
                bb = bitboard & (bitboard >> direction);
                if ((bb & (bb >> (2 * direction))) != 0) return true;
            }
            return false;
        }
        '''
        bb = self._bitboard[player]

        for d in [1, 7, 6, 8]:
            b = bb & (bb >> d)
            if (b & (b >> (2 * d))) != 0:
                return True
        return False

    def listMoves(self):
        '''
        @brief List all possible moves in a given situation
        int[] moves;
        long TOP = 1000000_1000000_1000000_1000000_1000000_1000000_1000000L;
        for(int col = 0; col <= 6; col++) {
            if ((TOP & (1L << height[col])) == 0) moves.push(col);
        }
        return moves;
        '''
        # 6 13 20 27 34 41 48
#         top = 1 << 6 | 1 << 13 | 1 << 20 | 1 << 27 | 1 << 34 | 1 << 41 | 1 << 48
#         moves = list()
#         for i in range(7):
#             if (top & 1 << self._height[i]) == 0:
#                 moves.append(i)
#         return moves
        return [i for i in range(7) if self._column_count[i] > 0]

    def flatView(self):
        '''
        @brief Get flat view of the board
        @details flat size is based on bitboard size (49). To represent Connect Four board,
         index (6 13 20 27 34 41 48) should be remove from list. 
        '''
        view = self._flat[:]
        for i in (48, 41, 34, 27, 20, 13, 6):
            view.pop(i)
        return view

    def __str__(self):
        s = '\n'
        bbx = self._bitboard[0]
        bbo = self._bitboard[1]

        for i in range(5, -1, -1):
            for j in range(0 + i, 47 + i, 7):
                if (bbx >> j) & 1:
                    s += 'x'
                elif (bbo >> j) & 1:
                    s += 'o'
                else:
                    s += '-'
            s += '\n'
        return s
