import pytest

# Check if all characters are unique in a string

# Brute force O(N^2):

def unique(s1):
    for char1 in s1:
        count = 0
        for char2 in s1:
            if char1 == char2:
                count += 1
            if count == 2:
                return False
    return True

# Hash Table O(N) run time, O(1) space (assuming ASCII characters):

def unique_hash(s1):
    checker = {}
    for char in s1:
        checker[char] = 0
    for char in s1:
        checker[char] += 1
        if checker[char] == 2:
            return False
    return True

def test_answer():
    assert unique('abc') == True
    assert unique('abca') == False

    assert unique_hash('abc') == True
    assert unique_hash('abca') == False