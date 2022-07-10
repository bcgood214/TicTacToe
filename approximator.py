import helper, random
from generalize import *

class Approx:
    def __init__(self):
        self.states = {}
        self.generals = {}
    
    def find_match(self, state, values):
        best, value = random.choice(list(self.generals.items()))
        while value[-1] != values[-1] or value[-2] != values[-2]:
            best, value = random.choice(list(self.generals.items()))
        print("best: {}; value: {}".format(best, value))
        
        value = compare(value, values)
        for k in self.generals:
            if self.generals[k][-1] == values[-1] and self.generals[k][-2] == values[-2]:
                diff = compare(self.generals[k], values)
                if diff < value:
                    value = diff
                    best = k
        
        return best

if __name__ == "__main__":
    appr = Approx()
    appr.generals['a'] = 10
    appr.generals['b'] = 20
    appr.generals['c'] = 30
    appr.find_match(20, 30)
