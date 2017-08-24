
'''
astar.py
author : rusty
date : 24/08/2017
'''

import random
from environments import EightPuzzle


class UCSAgent:
    '''
    An instance of UCSAgent is an object which can recieve percepts from
    an environment and take an action to maximize its performance measure
    by planning its way from initial state to the goal.

    Strategy: Expand the lowest cost node. 
    Implementation: the frontier is a priority queue where lowest cost node has the highest priority. 
    In order to be optimal, must test at expansion.



    Search Strategy : Uniform Cost Search 
    '''

    def __init__(self):
        self.frontier = list() # a list of all nodes that are generated but not explored
        self.explored = list() # set of all the visited states
        self.plan = list() # a sequence of actions to reach the goal


    def insert_by_order(self, current):
        '''
        inserts current into the frontier (sorted) at an appropriate position
        '''
        i = 0
        while( i < len(self.frontier) and current.path_cost >= self.frontier[i].path_cost ):
            i += 1

        self.frontier.insert(i, current)


    def find_solution(self, initial, goal):
        '''
        given the agent's initial state and desired goal state,
        returns a sequence of actions to reach the goal from the initial
        state.
        '''

        self.insert_by_order(initial)

        while(True):
            if(len(self.frontier)==0):
                return self.plan

            current = self.frontier.pop(0)
            self.explored.append(current.state)

            if(current.goal_test(goal)):
                while(current):
                    self.plan.insert(0,current.state)
                    current = current.parent
                return  self.plan

            actions = current.actions()

            for action in actions:
                child = current.transistion(action)
                if child.state not in self.explored:
                    self.insert_by_order(child)

        return self.plan

if __name__ == '__main__':
    # run some tests
    
    test_agent = UCSAgent()
    initial = EightPuzzle(initial_state=['1','4',' ','3','2','8','5','6','7']) # a solvable initial state for testing purposes
    goal = EightPuzzle(goal=True)
    plan = test_agent.find_solution(initial, goal)
    for each_state in plan:
        print("------")
        for i in range(0,9,3):
            print("{} {} {}".format(each_state[i],each_state[i+1],each_state[i+2]))
