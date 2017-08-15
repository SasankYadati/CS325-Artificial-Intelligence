'''
environment8puzzle.py
author : happystick
date : 14/08/2017
'''

import random
class environment:
    '''
    The environment is a 8puzzle board. Each cell
    contains a number from 1 to 8 or is empty.

    The initial state of the environment is a random configuration
    of the tiles in the 3x3 board.

    A state of an environment is the configuration of the
    environment at a particular instance.

    Possible Actions in this Environment : Up, Down, Right, Left

    Every state remembers the path cost it took to reach the current
    state from the initial state.

    Every state has a reference to the it's parent (state from which it
    has been resulted from).
    '''

    def __init__(self, initial_state):
        if initial_state:
            self.state = initial_state
        else:
            # initialize all the cells randomly
            self.state = [' ','1','2','3','4','5','6','7','8']
            random.shuffle(self.state)

        self.path_cost = 0
        self.parent = None


    def actions(self):
        '''
        recieves an object of type environment, which describes
        a state of the environment.

        returns a set of actions that can be taken in this state.

        the set of actions that can be taken depends on the position
        of the blank tile on the board.
        '''

        actions = list()

        blank_pos = self.state.index(' ')

        if blank_pos==0:
            actions.append('DOWN')
            actions.append('RIGHT')
        elif blank_pos==1:
            actions.append('LEFT')
            actions.append('DOWN')
            actions.append('RIGHT')
        elif blank_pos==2:
            actions.append('LEFT')
            actions.append('DOWN')
        elif blank_pos==3:
            actions.append('UP')
            actions.append('DOWN')
            actions.append('RIGHT')
        elif blank_pos==4:
            actions.append('UP')
            actions.append('LEFT')
            actions.append('DOWN')
            actions.append('RIGHT')
        elif blank_pos==5:
            actions.append('UP')
            actions.append('LEFT')
            actions.append('DOWN')
        elif blank_pos==6:
            actions.append('UP')
            actions.append('RIGHT')
        elif blank_pos==7:
            actions.append('UP')
            actions.append('LEFT')
            actions.append('RIGHT')
        elif blank_pos==8:
            actions.append('UP')
            actions.append('LEFT')
        else:
            print("ERROR!!")

        return actions

    def transistion(self,action):
        '''
        assumes "action" is valid in self.state.

        performs "action" on self.state and
        returns the resulting state.
        '''

        result = environment()

        for i in range(0, 9):
            result.state[i] = self.state[i]

        blank_pos = self.state.index(' ')

        if action=='UP':
            result.state[blank_pos] = result.state[blank_pos-3]
            result.state[blank_pos-3] = ' '
        elif action=='LEFT':
            result.state[blank_pos] = result.state[blank_pos-1]
            result.state[blank_pos-1] = ' '
        elif action=='DOWN':
            result.state[blank_pos] = result.state[blank_pos+3]
            result.state[blank_pos+3] = ' '
        elif action=='RIGHT':
            result.state[blank_pos] = result.state[blank_pos+1]
            result.state[blank_pos+1] = ' '

        result.parent = self
        result.path_cost = self.path_cost + 1

        return result

    def goal_test(self):
        '''
        returns True, if the state is a goal state, False otherwise.

        '''
        i = 1
        while i<=8 and self.state[i]==str(i):
            i += 1
        if i<=8:
            return False
        return True


if __name__=='__main__':
    print('Running tests')

    curr_state = environment()
    actions = curr_state.actions()
    new_state = curr_state.transistion(action=actions[0])

    # print the states
    print("Current state : {}".format(curr_state.state))
    print("Resulting state : {}".format(new_state.state))

    # print the actions
    print("Actions on current state : {}".format(actions))
    print("Actions on resulting state : {}".format(new_state.actions()))

    # print the path costs
    print("Path cost of curr_state : {}".format(curr_state.path_cost))
    print("Path cost of resulting state : {}".format(new_state.path_cost))

    # create a goal state for testing purposes
    goal = environment()
    goal.state = [' ', '1', '2', '3', '4', '5', '6', '7', '8']

    # testing goal_test() function
    print("Goal test on a goal state : {}".format(goal.goal_test()))
    print("Goal test on current state : {}".format(curr_state.goal_test()))
    print("Goal test on resulting state : {}".format(new_state.goal_test()))
