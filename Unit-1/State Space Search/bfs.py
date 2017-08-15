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
    '''

    def __init__(self):
        self.frontier = deque() # append() and popleft()
        self.explored = set() # add() and remove()
        self.plan = deque() # a sequence of actions to reach the goal

    def find_solution(self, initial_state, goal_state):
        '''
        given the agent's initial state and desired goal state,
        returns a sequence of actions to reach the goal from the initial
        state.
        '''

        pass

        return self.plan

if __name__ == '__main__':
    # run some tests
    pass
