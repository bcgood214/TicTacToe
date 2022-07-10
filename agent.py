from itertools import permutations
import helper, random
from approximator import Approx
from generalize import sum

class Agent:
    def __init__(self, epsilon=0.1, alpha = 0.1, approx=False):
        self.states = {}
        self.approx = Approx()
        if not approx:
            for state in helper.states():
                mat = helper.strtomat(state)
                if helper.check_game(mat):
                    if helper.has_won(mat, 'x'):
                        self.states[state] = 1.0
                    else:
                        self.states[state] = 0.0
                        # if state == "oxoxoxonn":
                        #     print(state)
                else:
                    self.states[state] = 0.5

        self.epsilon = epsilon
        # Note: The learning rate
        self.alpha = alpha
        self.last = None
    
    def best_known(self, state):
        topval = -0.5
        known_best = None
        next_states = helper.get_next_states(state, 'x')
        for ns in next_states:
            if self.states[ns] > topval:
                known_best = ns
                topval = self.states[ns]
        
        return known_best
    
    def best_known_approx(self, state):
        topval = -0.5
        known_best = None
        best_approx = None
        next_states = helper.get_next_states(state, 'x')
        for ns in next_states:
            ns_approx = self.insert_approx(ns)
            if self.states[ns_approx] > topval:
                known_best = ns
                topval = self.states[ns_approx]
                best_approx = ns_approx
        
        return known_best, best_approx
    
    # Returns True if the state is already in the generalization table, False otherwise
    def check_approx(self, state):
        if state not in self.approx.generals:
            val = sum(helper.strtomat(state), 'x')
            self.approx.generals[state] = val
            return False
        return True
    
    def insert_approx(self, state):
        approx_state = None
        board = helper.strtomat(state)

        if len(self.approx.generals) < 1000:
            preex = self.check_approx(state)
            approx_state = state
            if not preex:
                if helper.check_game(board):
                    if helper.has_won(board, 'x'):
                        self.states[approx_state] = 1.0
                    else:
                        self.states[approx_state] = 0.0
                else:
                    self.states[approx_state] = 0.5
        else:
            approx_state = self.approx.find_match(state, sum(board))
        
        return approx_state


    def move(self, board, explore=True):
        state = board
        if isinstance(board, list):
            state = helper.state_strrep(state)
        
        approx_state = self.insert_approx(state)

        
        if self.states[approx_state] == 0.0 or self.states[approx_state] == 1.0:
            if self.last is not None:
                self.states[self.last] = self.states[self.last] + self.alpha*(self.states[approx_state] - self.states[self.last])
            return state
        
        next_state, ns_approx = self.best_known_approx(state)

        if random.random() < self.epsilon and explore:
            next_state = random.choice(helper.get_next_states(state, 'x'))
            self.last = None
        else:
            # if next_state == "oxoxooxxn":
            #     print(self.last)
            #     if self.last is not None:
            #         print(self.states[self.last])
            if self.last is not None:
                old_val = self.states[self.last]
                new_val = self.states[ns_approx]
                self.states[self.last] = old_val + self.alpha*(new_val - old_val)
            
            self.last = ns_approx
        
        return next_state



if __name__ == "__main__":
    a = Agent()
