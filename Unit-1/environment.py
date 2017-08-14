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

    def __init__(self):
        self.state = list()
        # initialize all the cells with -1
        for i in range(0,9):
            self.state.append('-1')

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

        blank_pos = self.state.find(' ')

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

        result_state = environment()

        for i in range(0, 9):
            result_state.state[i] = self.state[i]

        pass
