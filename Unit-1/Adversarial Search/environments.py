'''
environments.py
author : happystick
date : 14/08/2017
'''

class TicTacToe:
    '''
    The environment is a Tic Tac Toe board.
    Each cell is either marked with an 'O' or a 'X' or is empty.

    The initial state of the environment is an empty 3x3 board.

    Possible actions in this environment : 1,2,...9 ( positions on the board ).

    Every state is associated with some utility for a given player.

    Every state has a reference to it's parent (state from which it
    has been resulted from).
    '''
