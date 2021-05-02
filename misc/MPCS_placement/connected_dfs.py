# https://uchicago.kattis.com/problems/uchicagoplacement.connected
# Staying Connected 2015-2016 Placement Exam

def dfs(pairs, root_vertex):
    verticies[root_vertex] = 'visited'
    for pair in pairs:
        if root_vertex in pair:
            if pair[0] != root_vertex:
                if verticies[pair[0]] != 'visited':
                    dfs(pairs, pair[0])
            else:
                if verticies[pair[1]] != 'visited':
                    dfs(pairs, pair[1])

V = int(input())  # Number of Verticies
E = int(input())  # Number of Edges

if E == 0:
    print(V)
    exit()

pairs = []
for i in range(E):
    x, y = map(int, input().split())
    pairs.append([x, y])

verticies = {}

for pair in pairs:
    verticies[pair[0]] = ''
    verticies[pair[1]] = ''

count = 0
for i in range(V):
    if i in verticies.keys():
        if verticies[i] != 'visited':
            count += 1
    else:
        count += 1
    dfs(pairs, i)
    
print(count)