import helper

def pieces(board, piece):
    count = 0
    for row in board:
        for item in row:
            if item == piece:
                count += 1
    
    return count

def two(board, piece):
    count = 0
    for row in board:
        row_count = 0
        for item in row:
            if item == piece:
                row_count += 1
        
        if row_count >= 2:
            count += 1
    
    return count

def r1_count(board, piece):
    return board[0].count(piece)

def r2_count(board, piece):
    return board[1].count(piece)

def r3_count(board, piece):
    return board[2].count(piece)

def d1_count(board, piece):
    d1 = [board[0][0], board[1][1], board[2][2]]

    return d1.count(piece)

def d2_count(board, piece):
    d2 = [board[0][2], board[1][1], board[2][0]]

    return d2.count(piece)

def c1_count(board, piece):
    c1 = [board[i][0] for i in range(3)]

    return c1.count(piece)

def c2_count(board, piece):
    c2 = [board[i][1] for i in range(3)]

    return c2.count(piece)

def c3_count(board, piece):
    c3 = [board[i][2] for i in range(3)]

    return c3.count(piece)

def sum(board, piece):
    sum = []
    sum.append(r1_count(board, piece))
    sum.append(r2_count(board, piece))
    sum.append(r3_count(board, piece))
    sum.append(d1_count(board, piece))
    sum.append(d2_count(board, piece))
    sum.append(c1_count(board, piece))
    sum.append(c2_count(board, piece))
    sum.append(c3_count(board, piece))

    return sum

def compare(sumx, sumy):
    diff = 0
    for i in range(len(sumx)):
        diff += abs(sumx[i] - sumy[i])
    
    return diff

if __name__ == "__main__":
    b1 = "n"*9
    b2 = "n"*3 + "x"*3 + "o"*3
    s1 = helper.strtomat(b1)
    s2 = helper.strtomat(b2)

    print(r3_count(s1, 'x'))
    print(c3_count(s2, 'o'))