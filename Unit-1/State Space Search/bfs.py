'''
bfs.py
author : happystick
date : 14/08/2017
'''

from environment import environment
from collections import deque

class BFSAgent:
    '''
    An instance of BFSAgent is an object which can recieve percepts from
    an environment and take an action to maximize its performance measure
    by planning its way from initial state to the goal..

    Search Strategy : Breadth First Search

    The agent additionally uses data structures like queue and set.
    '''

    def __init__(self):
        self.frontier = deque() # append() and popleft()
        self.explored = set() # add() and remove()

    def compute_action(self, curr_state):
        '''
        returns the best possible action to reach the goal using the plan
        computed by Breadth First Search.
        '''

        if curr_state.goal_test():
            # reached the goal state
            # do nothing
            return None

        possible_actions = curr_state.actions()

        action = ''

        pass

        return action

    def find_path(self, initial_state, goal_state):
        '''
        given the agent's initial state and desired goal state,
        returns a sequence of actions to reach the goal from the initial
        state.
        '''

        # a sequence of actions to be taken in order to reach the goal
        action_plan = list()

        pass

        return action_plan

if __name__ == '__main__':
    # run some tests
    pass
