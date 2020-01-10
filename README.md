# Py Board Games

Classic board games written in Python using Console as GUI.
AI opponent is using MinMax algorithm.

## Games available

- TicTacToe
- Connect Four


# Test

    $ cd py_board_games
    $ python -m unittest -v
    
# ToDo

- [ ] Add history to Board
- [ ] Profile TicTacToe implementation for optimization
- [ ] Setup Continuous Integration
- [ ] Speed up computation by removing bound checking and use exception, IndexError: out of range
- [ ] Make Minmax using thread
- [x] Evaluate leaf point in respect to current depth
- [x] Add AI using MinMax algorithm
- [x] Add unittest for Minmax
- [x] Do not evaluate for winner when less than 5 token have been played
- [x] Add user input to select Ai vs Human
- [x] Measure time needed to evaluate next move with Minmax
- [x] Add Minmax AlphaBeta
- [x] Factorize ressources between games
- [x] Add Connect Four game

# Optimization

- [x] Connect Four: Compute end game only considering last move and its impact

# Links

## Tree

* https://anytree.readthedocs.io/en/2.7.3/

## Minmax

* https://stackabuse.com/minimax-and-alpha-beta-pruning-in-python/
* https://github.com/Cledersonbc/tic-tac-toe-minimax
* https://www.ntu.edu.sg/home/ehchua/programming/java/JavaGame_TicTacToe_AI.html
* https://www.codeproject.com/Articles/43622/Solve-Tic-Tac-Toe-with-the-MiniMax-algorithm

# Other board games

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
