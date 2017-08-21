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

    Possible actions in this environment : 1,2,...,8,9 ( positions on the board ).

    Every terminal state is associated with some utility for both players.

    Every state has a reference to its parent (state from which it
    has been resulted from).

    This is an adversarial environment. 'X' always goes first.
    ->Fully observable
    ->Deterministic
    ->Discrete
    ->Static
    ->Sequential
    '''

    def __init__(self):
        self.state = [' ' for x in range(0,9)]

        pass

    def actions(self):
        '''
        recieves an object of type environment, which describes
        a state of the environment.

        returns a set of actions that can be taken in this state.

        the set of actions that can be taken depends on the position
        of the X's and O's on the board.
        '''

        actions = list()

        return actions

    def player(self):
        '''
        recieves an object of type environment, which describes
        a state of the environment.

        returns 'X' or 'O' by determining the player who holds the turn.
        '''

        pass

    def transistion(self,action):
        '''

        '''
        pass

    def terminal_test(self):
        '''

        '''
        pass

    def
