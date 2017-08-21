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
        self.state = [' ' for _ in range(0,9)]

    def actions(self):
        '''
        recieves an object of type environment, which describes
        a state of the environment.

        returns a set of actions that can be taken in this state.

        the set of actions that can be taken depends on the position
        of the X's and O's on the board.
        '''

        actions = list()
        for i in range(0,9):
            if self.state[i]==' ':
                actions.append(i+1)
        return actions

    def player(self):
        '''
        recieves an object of type environment, which describes
        a state of the environment.

        returns 'X' or 'O' by determining the player who holds the turn.
        '''
        # count no. of X's
        x_count = self.state.count('X')
        # count no. of O's
        o_count = self.state.count('O')
        if(x_count==o_count):
            return 'X'
        else:
            return 'O'
        pass

    def transistion(self,action):
        '''
        assumes "action" is valid in self.state.

        performs "action" on self.state and returns the resulting state.
        '''

        result = TicTacToe()
        result.state = list(self.state)
        result.state[action-1] = result.player()

        return result

    def terminal_test(self):
        '''
        returns true if self.state is an end state for the environment, false otherwise.
        '''
        # for all rows
        for i in range(0,7,3):
            if self.state[i]!=' ' and self.state[i]==self.state[i+1] and self.state[i+1]==self.state[i+2]:
                return True
        # for all columns
        for i in range(0,3):
            if self.state[i]!=' ' and self.state[i]==self.state[i+3] and self.state[i+3]==self.state[i+6]:
                return True

        # for the two diagonals
        if self.state[0]!=' ' and self.state[0]==self.state[4] and self.state[4]==self.state[8]:
            return True

        elif self.state[2]!=' ' and self.state[2]==self.state[4] and self.state[4]==self.state[6]:
            return True

        if self.state.count(' ') > 0:
            return False

        return True # draw state

    def utility(self,player):
        '''
        assumes self.state is a terminal state.

        returns the utility (score) for the player in self.state.
        '''
        pass

if __name__ == '__main__':
    # Testing purposes
    initial = TicTacToe()
    new = initial.transistion(initial.actions()[0])

    print("Actions on \n {} : \n {}".format(initial.state, initial.actions()))
    print("New state \n {} and actions on new state : \n {}".format(new.state, new.actions()))
    print("Player in new : {}".format(new.player()))
