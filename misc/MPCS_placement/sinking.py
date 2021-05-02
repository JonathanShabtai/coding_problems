# https://uchicago.kattis.com/problems/uchicago.mpcs.sinking
# That Sinking Feeling problem MPCS 2014-2015 Placement Exam

#N is the number of columns
#M is the number of rows
#S is the number of ships
#R is the number of shots

N, M, S, R = map(int, input().split())
score = 0
sunk_count = 0

def create_the_board(N,M):
    board = []
    board_row = []
    for i in range(M):
        for j in range(N):
            board_row.append("X")
        board.append(board_row)
        board_row = []
    return(board)

def closest_ship(board, x, y):
    min_dist = (N + M)
    for i in range(M):
        for j in range(N):
            try:
                board[i][j] == "Ship"
            except:
                pass
            else:
                if board[i][j] == "Ship":
                    dist = (abs(j - y) + abs(i - x))
                    if dist < min_dist:
                        min_dist = dist
    return(min_dist)

board = create_the_board(N,M)

for ship in range(S):
    x, y = map(int, input().split())
    board[x][y] = "Ship"

for shot in range(R):
    x, y = map(int, input().split())
    if board[x][y] == "Ship":
        board[x][y] = "HIT"
        score += 1000
        sunk_count += 1
    else:
        board[x][y] = "MISS"
        D = closest_ship(board, x, y)
        score += max(0, 1000 - D * 100)

print(f'{sunk_count}/{S} ships sunk. Score: {score} points')