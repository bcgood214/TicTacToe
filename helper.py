import re, itertools

# returns False if the game is not over, True if it is
def check_game(board):
    for row in board:
        if None not in row:
            if 'x' not in row or 'o' not in row:
                return True
    
    columns = [[board[0][i], board[1][i], board[2][i]] for i in range(3)]
    # print(columns)

    for col  in columns:
        if None not in col:
            if 'x' not in col or 'o' not in col:
                return True
    
    # check the diagonals
    d1 = [board[0][0], board[1][1], board[2][2]]
    d2 = [board[0][2], board[1][1], board[2][0]]

    # print(d1)
    # print(d2)

    if None not in d1:
        if 'x' not in d1 or 'o' not in d1:
            return True
    
    if None not in d2:
        if 'x' not in d2 or 'o' not in d2:
            return True
    
    empty_spaces = False
    for row in board:
        if None in row:
            empty_spaces = True
            break
    
    # if there are spaces empty, the game can be continued
    if empty_spaces:
        return False
    
    return True

def find_next(currstate, board):
    matcher = currstate.replace('n', '.')
    matches = []
    for config in board:
        if re.search(matcher, config):
            matches.append(config)
    
    return matches

def get_next_states(state, piece):
    start = 0
    ind = state.find('n', start)
    states = []
    while ind != -1:
        new = list(state)
        new[ind] = piece
        states.append(''.join(new))
        start = ind+1
        ind = state.find('n', start)
    
    return states





# Check if the player (RL agent) has won
def has_won(board, piece):
    other_piece = 'o'
    if piece == 'o':
        other_piece = 'x'
    
    for row in board:
        if None not in row and other_piece not in row:
            return True
    
    columns = [[board[0][i], board[1][i], board[2][i]] for i in range(3)]

    for col in columns:
        if None not in col and other_piece not in col:
            return True
    
    d1 = [board[0][0], board[1][1], board[2][2]]
    d2 = [board[0][2], board[1][1], board[2][0]]

    if None not in d1 and other_piece not in d1:
        return True
    elif None not in d2 and other_piece not in d2:
        return True
    
    return False

def state_strrep(board):
    strstate = ""
    for row in board:
        for item in row:
            if item is None:
                strstate += 'n'
            elif item == 'x':
                strstate += 'x'
            else:
                strstate += 'o'
    
    return strstate


# Note: should probably implement a function to convert string representation to matrix/list
def strtomat(s):
    state = [[], [], []]
    i = 0
    for char in s:
        ind = None
        if i >= 6:
            ind = 2
        elif i >= 3:
            ind = 1
        else:
            ind = 0
        
        if char == 'n':
            state[ind].append(None)
        else:
            state[ind].append(char)
        
        i += 1
    
    return state

def states():
    mylist = ['x', 'o', 'n']
    mylist = list(itertools.product(mylist, repeat=9))
    states = []

    for item in mylist:
        state = ''
        for char in item:
            state += char
        states.append(state)
    
    return states

# Note: genstates no longer considered a relevant function
# def genstates():
#     first_state = "n"*9
#     second_state = "x" + "n"*8
#     third_state = "o" + "n"*8
#     states = [first_state, second_state, third_state]

#     x = 0
#     while len(states) < 3**9:
#         l = len(states)
#         ind = ((l+x)//3)-1
#         str_ind = (3+x)//3
#         if str_ind > 8:
#             str_ind = 8
#         childone = states[ind]
#         childtwo = states[ind]

#         childone_list = list(childone)
#         childone_list[str_ind] = 'x'
#         childone = ''.join(childone_list)

#         childtwo_list = list(childtwo)
#         childtwo_list[str_ind] = 'o'
#         childtwo = ''.join(childtwo_list)

#         states.append(childone)
#         states.append(childtwo)

#         x += 1

#     return states


if __name__ == "__main__":
    pass