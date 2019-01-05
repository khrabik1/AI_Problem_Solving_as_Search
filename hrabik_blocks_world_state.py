from random import shuffle

class blocks_world_state:
    

    def __init__(self, blocks, goal):

        self.blocks = blocks.copy()


        self.goal = goal

    
    def __str__(self):
        answer = ' '
        for i in range(3):
            answer += '{} '.format(self.blocks[i])
            if (i+1)%3 == 0:
                answer += '\n'
        return answer

    
    def __eq__(self, other):
        return self.blocks == other.blocks

    def __hash__(self):
        return hash(self.blocks[0])

  
    def __lt__(self,other):
        return self.evaluation() < other.evaluation()

    
    
    def successors(self):
        
        successor_states = []
        
        for item in list(self.blocks):
            
            if len(item) > 1:
              
                successor_list = list(self.blocks)
                
                
                this_item = item[0]
           
                successor_list.remove(item)
                
              
                successor_list.append(item.strip(this_item))
                
                
                successor_list.append(this_item)
                
        
                new_state = blocks_world_state(successor_list, self.goal)
                
                
                successor_states.append(new_state)
                                      
            elif len(item) == 1:
                
                for thing in list(self.blocks):
                    
                    if thing == item:
                        pass
                    else:
                        
                        successor_list = list(self.blocks)
                        
                        
                        new_stack = item + str(thing)
                        
                        
                        successor_list.remove(item)
                        successor_list.remove(thing)
                        
                        
                        successor_list.append(new_stack)
                        
                        
                        new_state = blocks_world_state(successor_list, self.goal)
                        
                       
                        successor_states.append(new_state)
                                      
        return successor_states
                        


    
    def evaluation(self):
        wrong = 0
        
        for item in self.goal:
            
            for letter in item:
                
                for existingItem in self.blocks:
                    
                    for existingLetter in existingItem:
                        
                        if existingLetter == letter and item.find(letter) != existingItem.find(existingLetter):
                            wrong += 1
        return wrong

    



def search(start, strategy, max_states, states_so_far=0):
    to_visit = [ start ]
    goal = start.goal
    already_visited = set()
    verbose = False
    while to_visit != [ ]:
        #       input('anything\n')
        state = to_visit.pop(-1)
        #       print('current state\n{}'.format(state))
        if set(state.blocks) == set(goal):
            return states_so_far
        elif states_so_far >= max_states:
            return states_so_far
        elif set(state.blocks) in set(already_visited):
            pass
        else:
            already_visited.add(frozenset(state.blocks))
            new_states = state.successors()
            shuffle(new_states)
            if strategy == 'dfs':
                to_visit = to_visit + new_states
            elif strategy == 'bfs':
                to_visit = new_states + to_visit
            elif strategy == 'best':
                total_states = to_visit + new_states
                to_visit = sorted(total_states, reverse=True)
            states_so_far += 1
    return states_so_far





start = input("Enter a start state, with items separated by commas: ")
goal = input("Enter a goal state in the same format: ")

start = list(start.split(","))
goal = list(goal.split(","))

startState = blocks_world_state(start, goal)

print("States checked for DFS: {}".format(search(startState, 'dfs', 2000, 0)))
print("States checked for BFS: {}".format(search(startState, 'bfs', 2000, 0)))
print("States checked for Best: {}".format(search(startState, 'best', 2000, 0)))
