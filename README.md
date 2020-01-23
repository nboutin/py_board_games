# Py Board Games

Classic board games written in Python using Console as GUI.
AI opponent is using MinMax Alpha Beta algorithm.

## Games available

- TicTacToe
- Connect Four
- Gomoku aka 5 in row

# Test

    $ cd py_board_games
    $ python -m unittest -v
    
# ToDo
## Feature
- [ ] Print moves history

## Optimization

- [ ] Implement bitboard
- [ ] Improve evaluate function by counting 3 token in a row of 4, take into account empty cell

## Design / Technical choice
- [ ] MinMax use current depth and depth_max parameters
- [ ] Define base class Game
- [ ] Construct TicTacToe game from Gomoku with configuration

## Tests
- [ ] Add unittest for game selection/configuration in main
- [ ] Setup Continuous Integration

## Fix
- [ ] Handle bad user input

## Documentation to read
- [ ] https://github.com/denkspuren/BitboardC4/blob/master/BitboardDesign.md
- [ ] https://towardsdatascience.com/creating-the-perfect-connect-four-ai-bot-c165115557b0
- [ ] https://github.com/aimacode/aima-python/blob/master/games.py


# Links

## Tree

* https://anytree.readthedocs.io/en/2.7.3/

## Minmax

* https://stackabuse.com/minimax-and-alpha-beta-pruning-in-python/
* http://www.pressibus.org/ataxx/autre/minimax/paper.html
* https://github.com/Cledersonbc/tic-tac-toe-minimax
* https://www.ntu.edu.sg/home/ehchua/programming/java/JavaGame_TicTacToe_AI.html
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
