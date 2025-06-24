import math
def print_board(board):
    for row in board:
        print("|".join(row))
        print("_" *5)

def check_winner(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] !="":
            return board[i][0]
        if board[0][i] ==  board[1][i] == board[2][i] !="":
            return board[0][i]

        if board[0][0] == board[1][1] == board[2][2] !="":
            return board[0][0]
        if board[0][2] == board[1][1] == board[2][0] !="":
            return board[0][2]

    return None

def is_board_full(board):
    return all(cell != "" for row in board for cell in row)

def minimax(board, depth, is_maximizing):
    winner = check_winner(board)
    if winner == "X":
        return 1
    if winner == "O":
        return -1
    if is_board_full(board):
        return 0
    if is_maximizing:
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == "":
                    board[i][j] = "X"
                    score = minimax(board, depth + 1,False)
                    board[i][j] = ""
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == "":
                    board[i][j] = "O"
                    score = minimax(board, depth + 1,True)
                    board[i][j] = ""
                    best_score = min(score, best_score)
        return best_score

def best_move(board):
    best_score = -math.inf
    move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == "":
                board[i][j] = "X"
                score =  minimax(board,0,False)
                board[i][j] =""

            if score>best_score:
                move = (i,j)
    return move

def play_game():
    board = [["" for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while True:
        row = int(input("Enter the row (0, 1, or 2): "))
        col = int(input("Enter the column (0, 1, or 2): "))
        if board[row][col] != "":
            print("Cell already taken! Try again.")
            continue
        board[row][col] = "O"

        if check_winner(board) == "O":
            print_board(board)
            print("Congratulations! You win!")
            break

        if is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break

        move = best_move(board)
        if move:
            board[move[0]][move[1]] = "X"

        if check_winner(board) == "X":
            print_board(board)
            print("AI wins!")
            break

        if is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break

        print_board(board)

if __name__ == "__main__":
    play_game()

