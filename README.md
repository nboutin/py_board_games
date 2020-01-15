# Py Board Games

Classic board games written in Python using Console as GUI.
AI opponent is using MinMax algorithm.

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
- [x] Add Gomoku game aka 5 in row
- [x] Add user input to select Ai vs Human
- [x] Measure time needed to evaluate next move with Minmax
- [x] Add Connect Four game
- [x] Add Minmax AlphaBeta
- [x] Add history to Board
- [x] Evaluate leaf point by taken into account current depth
- [x] Add AI using MinMax algorithm

## Optimization

- [ ] Make Minmax using thread
- [ ] Improve check diag line by using last move value
- [ ] Speed up computation by removing bound checking and use exception, IndexError: out of range
- [ ] Try numpy Array for Board to improve performance
- [x] Profile Gomoku implementation for optimization
- [x] Check line should take into account line_win_size
- [x] Generate moves available for a game position
- [x] Do not evaluate for TicTacToe winner when less than 5 token have been played
- [x] Connect Four: Compute end game only considering last move and its impact

## Design
- [ ] Define base class Game
- [ ] Construct TicTacToe game from Gomoku with configuration
- [x] Define Token in game_base module
- [x] Make ASCII_View a base class
- [x] Game implement generate_moves functions
- [x] Add Board last_move function
- [x] Factorize ressources between games

## Tests
- [ ] Add unittest for game selection/configuration in main
- [ ] Pass parameter to enable skipped perfo test
- [ ] Setup Continuous Integration
- [x] Add unittest for Minmax

## Fix
- [ ] Handle multiple user input types
- [ ] Handle bad user input



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
