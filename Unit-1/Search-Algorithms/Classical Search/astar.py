'''
astar.py
author : happystick
date : 14/08/2017
'''

from environments import EightPuzzle

class AStarAgent:
    '''
    An instance of AStarAgent is an object which can recieve percepts from
    an environment and take an action to maximize its performance measure
    by planning its way from initial state to the goal.

    Search Strategy : A* Search (using heuristics**)

    ** heuristics is a design characteristic which depends on the environment,
    but is defined by the agent.

    Heuristic : No. of misplaced tiles on the board for an EightPuzzle.
    '''

    def __init__(self):
        self.frontier = list() # a list of all nodes that are generated but not explored
        self.explored = list() # set of all the visited states
        self.plan = list() # a sequence of actions to reach the goal

    def heuristic(self, current):
        '''
        returns the computed herustic value for a given environment state.
        '''
        goal_state = EightPuzzle(goal=True) # returns a goal state

        heuristic_value = 0
        for i in range(0,9):
            if goal_state.state[i] != current.state[i]:
                heuristic_value+=1

        return heuristic_value

    def insert_by_order(self, current):
        '''
        inserts current into the frontier (sorted) at an appropriate position
        '''
        i = 0
        while( i < len(self.frontier) and current.path_cost + self.heuristic(current) >= self.frontier[i].path_cost + self.heuristic(self.frontier[i]) ):
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
    # test_agent = AStarAgent()
    # test_state = EightPuzzle(initial_state=[' ','1','2','3','4','5','6','8','7'])
    # print("Current state is : {}".format(test_state.state))
    # print("Heuristic value for current state : {}".format(test_agent.heuristic(test_state)))

    test_agent = AStarAgent()
    initial = EightPuzzle(initial_state=['1','4',' ','3','2','8','5','6','7']) # a solvable initial state for testing purposes
    goal = EightPuzzle(goal=True)
    plan = test_agent.find_solution(initial, goal)
    for each_state in plan:
        print("------")
        for i in range(0,9,3):
            print("{} {} {}".format(each_state[i],each_state[i+1],each_state[i+2]))
