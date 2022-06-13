from itertools import permutations
import helper

class Agent:
    def __init__(self):
        init_state = [[None, None, None] for i in range(3)]
        self.states = {helper.state_strrep(init_state): 0.5}
        currstate = init_state

        while True:
            newstate = [[currstate[h][0], currstate[h][1], currstate[h][2]] for h in range(3)]

            # variable to identify change of state, with 1 = 'x' being added, 2 = 'o' being added, and 0 = no change
            modifier = 0
            # check for empty spaces
            for i in range(3):
                for j in range (3):
                    if currstate[i][j] is None:
                        newstate[i][j] = 'x'
                        modifier = 1
                        if helper.check_game(newstate):
                            if helper.has_won(newstate, 'x'):
                                self.states[helper.state_strrep(newstate)] = 1.0
                            else:
                                self.states[helper.state_strrep(newstate)] = 0.0
                        else:
                            self.states[helper.state_strrep(newstate)] = 0.5
            
            if modifier == 0:
                for i in range(3):
                    for j in range (3):
                        if currstate[i][j] == 'x':
                            newstate[i][j] = 'o'
                            modifier = 2
                            if helper.check_game(newstate):
                                if helper.has_won(newstate, 'x'):
                                    self.states[helper.state_strrep(newstate)] = 1.0
                                else:
                                    self.states[helper.state_strrep(newstate)] = 0.0
                            else:
                                self.states[helper.state_strrep(newstate)] = 0.5
            

            if modifier == 0:
                break

            currstate = newstate



if __name__ == "__main__":
    a = Agent()
    i = 0
    for key in a.states:
        print(key)
        i += 1
        if i >= 20:
            break
