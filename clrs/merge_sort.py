def merge_sort(A, p, r):
    if p < r:
        q = (p + r) // 2
        merge_sort(A, p, q)
        merge_sort(A, q+1, r)
        print(f'Current state of A: {A}')
        merge(A, p, q, r)

    return A

def merge(A, p, q, r):
    """ Assume A[0..n/2] and A[n/2..n] are sorted
    """
    n_1 = q - p + 1
    n_2 = r - q
    print(f'Subset of A: {A[p:r+1]}')
    print(f'p: {p}, q: {q}, r: {r}')
    L = A[p:p+n_1]
    R = A[q+1:q+1+n_2]
    print(f'Left: {L}, Right: {R}')
    L.append(float('inf'))
    R.append(float('inf'))
    curr, i, j = p, 0, 0
    while not(L[i] == float('inf') and R[j] == float('inf')):
        if L[i] <= R[j]:
            A[curr] = L[i]
            i += 1
        else:
            A[curr] = R[j]
            j += 1
        curr += 1
    print(f'A in merge: {A}')
    return A

print(merge_sort([5, 2, 4, 6, 1, 3], 0, 5))
