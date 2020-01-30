# Py Board Games

Classic board games written in Python using Console as GUI.
AI opponent is using MinMax Alpha Beta algorithm.

## Games available

- TicTacToe
- Connect Four
- Gomoku aka 5 in row

## Neat

- https://neat-python.readthedocs.io/en/latest/

# Test

    $ cd py_board_games
    $ python -m unittest -v
    
# ToDo
## Neat
- [ ] Profile evolve module
- [ ] Use Minmax_AB which return random moves when their are equals
- [ ] Start learning with only horizontal line to win, vertical, then diagonal
- [ ] Fitness function increase MinMax level when Neat wins

## Feature
- [x] Print moves history

## Optimization

- [ ] Improve alpha beta by exploring center column first (3,2,4,1,5,0,6)
- [ ] Improve evaluate function by counting 3 token in a row of 4, take into account empty cell
- [x] Implement bitboard
- [x] Check only row for the current player

## Design / Technical choice
- [ ] MinMax use current depth and depth_max parameters
- [ ] Define base class Game
- [ ] Construct TicTacToe game from Gomoku with configuration
- [x] Update ASCII_View to handle grid and bitboard representation

## Tests
- [ ] Add unittest for game selection/configuration in main
- [ ] Setup Continuous Integration

## Fix
- [ ] Handle bad user input

## Documentation to read
- [ ] https://github.com/denkspuren/BitboardC4/blob/master/BitboardDesign.md
- [ ] https://towardsdatascience.com/creating-the-perfect-connect-four-ai-bot-c165115557b0
- [ ] https://github.com/aimacode/aima-python/blob/master/games.py
- [ ] http://blog.gamesolver.org/solving-connect-four
- [ ] https://github.com/PascalPons/connect4


# Links

## Tree

* https://anytree.readthedocs.io/en/2.7.3/

## Minmax

* https://stackabuse.com/minimax-and-alpha-beta-pruning-in-python/
* http://www.pressibus.org/ataxx/autre/minimax/paper.html
* https://www.codeproject.com/Articles/43622/Solve-Tic-Tac-Toe-with-the-MiniMax-algorithm

# Other board games

* Gomoki (5 in row on 9*9 board)
* Othello
* Quixo / https://foxmind.co.il/uploads/70213732698722edfaf.pdf
* Ultimate TicTacToe / https://en.wikipedia.org/wiki/Ultimate_tic-tac-toe
* [Hex](https://fr.wikipedia.org/wiki/Hex)
* Chess
* Go
* Nim
* Le jeu de Dame
* Backgammon
* Reversi
* Checkers
* Mancala
