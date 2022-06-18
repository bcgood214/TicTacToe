from itertools import permutations
import helper, random

class Agent:
    def __init__(self, epsilon=0.1, alpha = 0.1):
        self.states = {}
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


    def move(self, board, explore=True):
        state = board
        if isinstance(board, list):
            state = helper.state_strrep(state)

        
        if self.states[state] == 0.0 or self.states[state] == 1.0:
            if self.last is not None:
                self.states[self.last] = self.states[self.last] + self.alpha*(self.states[state] - self.states[self.last])
            return state
        
        next_state = self.best_known(state)

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
                new_val = self.states[next_state]
                self.states[self.last] = old_val + self.alpha*(new_val - old_val)
            
            self.last = next_state
        
        return next_state



if __name__ == "__main__":
    a = Agent()
