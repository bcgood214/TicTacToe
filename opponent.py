class Opponent:
    def __init__(self, piece='o'):
        self.piece = piece

    
    def check_rows(self, board):
        i = 0
        for row in board:
            enemy_pieces = False
            j = 0
            for place in row:
                if board[i][j] is not None and board[i][j] != self.piece:
                    enemy_pieces = True

                j += 1
            
            if not enemy_pieces:
                place_ind = 0
                for place in row:
                    if place is None:
                        return (i, place_ind)
                    place_ind += 1
            i += 1
    
    def check_cols(self, board):
        for i in range(3):
            enemy_pieces = False
            for j in range(3):
                if board[j][i] is not None and board[j][i] != self.piece:
                    enemy_pieces = True
            
            if not enemy_pieces:
                for j in range(3):
                    if board[j][i] is None:
                        return (j, i)
    
    def select_def(self, board):
        for i in range(3):
            for j in range(3):
                if board[i][j] == None:
                    return (i, j)



    
    def make_move(self, board):
        row_res = self.check_rows(board)
        if row_res is not None:
            board[row_res[0]][row_res[1]] = self.piece
            return
        
        col_res = self.check_cols(board)
        if col_res is not None:
            board[col_res[0]][col_res[1]] = self.piece
        else:
            pos = self.select_def(board)
            if pos is None:
                return None
            board[pos[0]][pos[1]]

        pos = self.select_def(board)
        if pos is None:
            return None
        board[pos[0]][pos[1]] = 'o'


if __name__ == "__main__":
    opp = Opponent()
    board = [['x', 'x', 'o'], ['o', None, 'o'], ['x', 'x', None]]
    opp.make_move(board)
    print(board)