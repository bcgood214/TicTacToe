import helper, random
from generalize import *

class Approx:
    def __init__(self):
        self.states = {}
        self.generals = {}
        self.won = {}
        self.lost = {}
        self.draw = {}
    
    def select_random(self, state, values):
        if values[-1] == 1:
            # print(self.lost)
            return random.choice(list(self.lost.items()))
        elif values[-2] == 1:
            # print(self.won)
            return random.choice(list(self.won.items()))
        elif values[-3] == 1:
            return random.choice(list(self.draw.items()))
        # print(list(self.generals.items()))
        return random.choice(list(self.generals.items()))
    
    def insert(self, state, values):
        if values[-1] == 1:
            self.lost[state] = values
        elif values[-2] == 1:
            self.won[state] = values
        elif values[-3] == 1:
            self.draw[state] = values
        else:
            self.generals[state] = values
    
    def search_dicts(self, best_known, value, values, dict):
        diff = compare(value, values)
        best = best_known
        for i in dict:
            x = compare(dict[i], values)
            if x < diff:
                diff = x
                values = dict[i]
                best = i
        
        return best
    
    def get_length(self, state):
        board = state
        if type(state) != list:
            board = helper.strtomat(state)
        if helper.has_won(board, 'x'):
            return len(self.won)
        elif helper.has_won(board, 'o'):
            return len(self.lost)
        elif helper.check_game(board):
            return len(self.draw)
        return len(self.generals)
    
    def check_approx(self, state):
        if state in self.generals:
            return True
        elif state in self.won or state in self.lost or state in self.draw:
            return True
        else:
            val = sum(helper.strtomat(state), 'x')
            if val[-1] == 1:
                self.lost[state] = val
            elif val[-2] == 1:
                self.won[state] = val
            elif val[-3] == 1:
                self.draw[state] = val
            else:
                self.generals[state] = val
            return False
    
    # TODO: fully accomodate terminal states
    def find_match(self, state, values):
        best, value = self.select_random(state, values)
        # print(value)
        # diff = compare(value, values)
        # print("best: {}; value: {}".format(best, value))
        
        # diff = compare(value, values)
        if values[-1] == 1:
            return self.search_dicts(best, value, values, self.lost)
        elif values[-2] == 1:
            return self.search_dicts(best, value, values, self.won)
        elif values[-3] == 1:
            return self.search_dicts(best, value, values, self.draw)
        else:
            # print(value)
            return self.search_dicts(best, value, values, self.generals)

if __name__ == "__main__":
    appr = Approx()
    init_state = "oxoooxxox"
    board = helper.strtomat(init_state)
    print(board)
    v = sum(board, 'x')
    appr.insert(init_state, v)
    print(v)
    print(appr.generals)
    print(appr.won)
    print(appr.lost)
