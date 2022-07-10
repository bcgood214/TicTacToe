import agent, helper
from opponent import Opponent

# Return a tuple with a boolean value representing a win (True) or a loss (False)
# and the terminal state
def play_game(agent, explore=True, show=False):
    initial_state = "n"*9
    board = helper.strtomat(initial_state)
    opp = Opponent()

    while True:
        opp.make_move(board)
        next_move = agent.move(board, explore)
        board = helper.strtomat(next_move)
        if helper.check_game(board):
            if helper.has_won(board, 'x'):
                return (True, board)
            else:
                return (False, board)
        


if __name__ == "__main__":
    a = agent.Agent(epsilon=0.001, alpha=0.1)
    for i in range(5):
        play_game(a)
        # if i % 1000 == 0:
        #     print("For iteration #{}".format(i))
        #     print(play_game(a, explore=False, show=True))
        #     print("END")
    
    # for state in a.states:
    #     if a.states[state] > 0.5 and a.states[state] < 1.0:
    #         print(state)
    
    print(play_game(a, explore=False))
    print(len(a.approx.generals))
    