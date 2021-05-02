def queensAttack(n, k, r_q, c_q, obstacles):
    moves_count = (n-1) + (n-1) + 
    
    # going down
    i = r_q + 1
    while i < n+1:
        if [i, c_q] in obstacles:
            break
        moves_count += 1
        i += 1

    # going up
    i = r_q - 1
    while i > 0:
        if [i, c_q] in obstacles:
            break
        moves_count += 1
        i -= 1

    # going right
    j = c_q + 1
    while j < n+1:
        if [r_q, j] in obstacles:
            break
        moves_count += 1
        j += 1

    # going left
    j = c_q - 1
    while j > 0:
        if [r_q, j] in obstacles:
            break
        moves_count += 1
        j -= 1

    # going left down
    i = r_q + 1
    j = c_q - 1
    while i < n+1 and j > 0:
        if [i, j] in obstacles:
            break
        moves_count += 1
        i += 1
        j -= 1

    # going right down
    i = r_q + 1
    j = c_q + 1
    while i < n+1 and j < n:
        if [i, j] in obstacles:
            break
        moves_count += 1
        i += 1
        j += 1

    # going left up
    i = r_q - 1
    j = c_q - 1
    while i > 0 and j > 0:
        if [i, j] in obstacles:
            break
        moves_count += 1
        i -= 1
        j -= 1

    # going right up
    i = r_q - 1
    j = c_q + 1
    while i > 0 and j < n+1:
        if [i, j] in obstacles:
            break
        moves_count += 1
        i -= 1
        j += 1
    
    return moves_count


x = queensAttack(5, 3, 4, 3, [[5, 5], [4, 2], [2, 3]])
print(x)

x = queensAttack(100000, 0, 4187, 5068, [])
print(x)