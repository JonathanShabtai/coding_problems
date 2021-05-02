# https://uchicago.kattis.com/problems/uchicago.mpcs.sinking
# That Sinking Feeling problem MPCS 2014-2015 Placement Exam

#N is the number of columns
#M is the number of rows
#S is the number of ships
#R is the number of shots

N, M, S, R = map(int, input().split())
score = 0
sunk_count = 0
board = []
shots = []
sunken = []

for ship in range(S):
    x, y = map(int, input().split())
    board.append([x, y])

for shot in range(R):
    x, y = map(int, input().split())
    shots.append([x, y])

flag = True

for i in range(R):
    D_min = N + M
    for j in range(S):
        if shots[i] == board[j]:
            score += 1000
            sunk_count += 1
            sunken.append(board[j])
            flag = False
        else:
            if board[j] not in(sunken):
                x2, y2 = shots[i]
                x1, y1 = board[j]
                D = (abs(x2 - x1) + abs(y2 - y1))
                if D < D_min:
                    D_min = D
    if flag:
        score += max(0, 1000 - D_min * 100)     
    flag = True

print(f'{sunk_count}/{S} ships sunk. Score: {score} points')