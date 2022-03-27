import pytest

# Check if a string is the permutation of the other

# Brute force O(N^2):

def perm(s1, s2):
    s1_list = list(s1)
    print(s1_list)
    for char in s2:
        if char in s1_list:
            for i in range(len(s1_list)):
                if s1_list[i] == char:
                    s1_list[i] = False
                    print(s1_list)
                    break
        else:
            return False
    return True

# Hash Table O(N) run time, O(1) space (assuming ASCII characters):

def perm_hash(s1, s2):
    checker = {}
    for char in s1:
        checker[char] = 0
    for char in s1:
        checker[char] += 1
    print(checker)
    for char in s2:
        if char in checker.keys():
            checker[char] -= 1
            print(checker)
        else:
            return False
    print(sum(checker.values()))
    if sum(checker.values()) != 0:
        return False
    return True

def test_answer():
    assert perm('abc', 'cba') == True
    assert perm('abc', 'abd') == False
    assert perm('abc', 'abcc') == False

    assert perm_hash('abc', 'cba') == True
    assert perm_hash('abc', 'abd') == False
    assert perm_hash('abc', 'abcc') == False