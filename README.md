# Py Board Games

Classic board games written in Python using Console as GUI.
AI opponent is using MinMax algorithm.

## Games available

- TicTacToe


# Test

    $ cd py_board_games
    $ python -m unittest -v
    
# ToDo

- [x] Evaluate leaf point in respect to current depth
- [x] Add AI using MinMax algorithm
- [x] Add unittest for Minmax
- [x] Do not evaluate for winner when less than 5 token have been played
- [x] Add user input to select Ai vs Human
- [x] Measure time needed to evaluate next move with Minmax
- [x] Add Minmax AlphaBeta
- [ ] Profile TicTacToe implementation for optimization
- [ ] Add Connect Four game
- [ ] Setup Continuous Integration
- [ ] Factorize ressources between games

# Optimization

- [ ] Compute end game only considering last move and its impact 

# Nice to Have
- [ ] Add Minmax Negamax
- [ ] Add Minmax Negascout

# Links

* https://stackabuse.com/minimax-and-alpha-beta-pruning-in-python/
* https://github.com/Cledersonbc/tic-tac-toe-minimax
* https://www.ntu.edu.sg/home/ehchua/programming/java/JavaGame_TicTacToe_AI.html
* https://www.codeproject.com/Articles/43622/Solve-Tic-Tac-Toe-with-the-MiniMax-algorithm

# Other board games

* [Hex](https://fr.wikipedia.org/wiki/Hex)
* Chess
* Go
* Nim
* Connect Four
* Le jeu de Dame
* Backgammon
* Reversi
* Checkers
* Mancala