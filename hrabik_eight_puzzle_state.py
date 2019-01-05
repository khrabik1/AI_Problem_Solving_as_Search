# CSC 380/480 Winter 2018
# A comparison of eight-puzzle using various forms of search.
# In this version, the evaluator for best-first is a count
# of the number of tiles that are in the correct position
# Built on a generalized state finder in search.py
#
# To run this, DO NOT load eight_puzzle_state.py -- instead, open
# search.py and press the F5 key to load it.

from random import shuffle    # to randomize the order in which successors are visited

class eight_puzzle_state:
    def __init__(self, tiles):
        self.tiles = tiles.copy()

        
        
    def __iter__(self):

        return iter(self.list)

    def __str__(self):
        answer = ''
        for i in range(9):
            answer += '{} '.format(self.tiles[i])
            if (i+1)%3 == 0:
                answer += '\n'
        return answer
    
    def __repr__(self):
        return 'eight_puzzle_state({})'.format(self.tiles)

    def __eq__(self, other):
        return self.tiles == other.tiles

    def __hash__(self):
        
        return hash(self.tiles[0])
        
    
    def successors(self):
        successor_states = [ ]
        neighbors = {0:[1,3],1:[0,2,4],2:[1,5],3:[0,4,6],4:[1,3,5,7],5:[2,4,8],6:[3,7],7:[4,6,8],8:[5,7]}
        zero_loc = self.tiles.index(' ')
        for loc in neighbors[zero_loc]:
            state = eight_puzzle_state(self.tiles)
            state.tiles[zero_loc] = state.tiles[loc]
            state.tiles[loc] = ' '
            successor_states.append(state)
        return successor_states

    # note: i ran your original evaluation with 10 trials to get data for your
    # estimator. then i replaced your estimator with mine and ran another 10
    # trials. Graph for review available as attachment. I feel like with more
    # trials this will be more more obviously efficient
   
    def evaluation(self):
        sumdistance = 0
 
        for i in range(9):
            num = goal_state().tiles[i]
            a = 0
       
            for tile in self.tiles:
                if tile == num:
                    sumdistance += abs((a // 3 + a % 3) - (i // 3 + i % 3))
                    a = 0
                    break
                else:
                    a += 1
        return sumdistance



    def __lt__(self, other):
        return self.evaluation() < other.evaluation()



        

    


def goal_state(ignore=None):
# something for goalState?
    return eight_puzzle_state(['1', '2', '3', '8', ' ', '4', '7', '6', '5'])

# from random import shuffle   random puzzle is too many moves from goal state
from random import randint

# make a start state which is n moves from goal state
def start_state(n=5):
    already_visited = [ goal_state() ]
    state = goal_state()
    # max number of moves from start state to goal state
    for i in range(n):
        successors = state.successors()
        for s in successors:
            if s in already_visited:
                successors.remove(s)
        shuffle(successors)
        state = successors[0]
        already_visited.append(state)
    return state




def random_eight_puzzle_state():
    tiles = ['1', '2', '3', '4', '5', '6', '7', '8', ' ']
    shuffle(tiles)
       
    return eight_puzzle_state(tiles)
