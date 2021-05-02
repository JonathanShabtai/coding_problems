# https://uchicago.kattis.com/problems/queens
# Verify This, Your Majesty 2013-2014 Placement Exam
# Jonathan Shabtai

def create_board(N):
    row = []
    board = []
    for i in range(N):
        for j in range(N):
            row.append("X")
        board.append(row)
        row = []
    return(board)

def check_queen(board, x, y, N):
    # Checking row
    if int(board[x].count("Q")) > 1:
        return(False)

    # Checking column
    col = []
    for i in range(N):
        col.append(board[i][y])
    if int(col.count("Q")) > 1:
        return(False)

    # Checking Diagonals (diag is top left to bottom right, diag2 is bottom left to top right)
    diag = []
    diag2 = []
    for i in range(N):
        if x + i < N and y + i < N:
            diag.append(board[x + i][y + i])
        if x - i >= 0 and y - i >= 0:
            diag.append(board[x - i][y - i])
        if x + i < N and y - i >= 0:
            diag2.append(board[x + i][y - i])
        if x - i >= 0 and y + i < N:
            diag2.append(board[x - i][y + i])
    if int(diag2.count("Q")) > 2:
        return(False)
    if int(diag.count("Q")) > 2:
        return(False)

    return(True)

board_size = int(input())
board = create_board(board_size)

for i in range(board_size):
    x, y = map(int, input().split())
    board[x][y] = "Q"

if board_size == 1:
    print("CORRECT")
    exit()

final_flag = True

for i in range(board_size):
    for j in range(board_size):
        if board[i][j] == "Q":
            if not(check_queen(board, i, j, board_size)):
                print("INCORRECT")
                final_flag = False
                break
    if not(final_flag):
        break

if final_flag:
    print("CORRECT")