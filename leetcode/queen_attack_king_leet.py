queens = [[5,6],[7,7],[2,1],[0,7],[1,6],[5,1],[3,7],[0,3],[4,0],[1,2],[6,3],[5,0],[0,4],[2,2],[1,1],[6,4],[5,4],[0,0],[2,6],[4,5],[5,2],[1,4],[7,5],[2,3],[0,5],[4,2],[1,0],[2,7],[0,1],[4,6],[6,1],[0,6],[4,3],[1,7]]
king = [3,4]

output_array = []
# going to the right
i = king[0]
while i < 8:
    if [i, king[1]] in queens:
        output_array.append([i, king[1]])
        break
    i += 1

# going to the left
i = king[0]
while i > -1:
    if [i, king[1]] in queens:
        output_array.append([i, king[1]])
        break
    i -= 1

# going down
j = king[1]
while j < 8:
    if [king[0], j] in queens:
        output_array.append([king[0], j])
        break
    j += 1

# going up
j = king[1]
while j > -1:
    if [king[0], j] in queens:
        output_array.append([king[0], j])
        break
    j -= 1

# going right up
i = king[0]
j = king[0]
while i < 8 and j > -1:
    if [i, j] in queens:
        output_array.append([i, j])
        break
    i += 1
    j -= 1

# going right down
i = king[0]
j = king[0]
while i < 8 and j < 8:
    if [i, j] in queens:
        output_array.append([i, j])
        break
    i += 1
    j += 1

# going left up
i = king[0]
j = king[0]
while i > -1 and j > -1:
    if [i, j] in queens:
        output_array.append([i, j])
        break
    i -= 1
    j -= 1

# going left down
i = king[0]
j = king[0]
while i > -1 and j < 8:
    if [i, j] in queens:
        output_array.append([i, j])
        break
    i -= 1
    j += 1

print(output_array)