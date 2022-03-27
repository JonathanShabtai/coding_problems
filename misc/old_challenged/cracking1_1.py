import numpy as np

def is_unique(word):
    dictionary = {}
    for letter in word:
        if letter not in dictionary.keys():
            dictionary[letter] = 1
        else:
            dictionary[letter] += 1

    for count in dictionary.values():
        if count > 1:
            return False

    return True

def is_unique_ascii(word):
    checker = np.zeros(128)
    for l in word:
        i = ord(l)
        checker[i] += 1
        if checker[i] > 1:
            return False

    return True

print(is_unique('abcde'))
print(is_unique('abcdeb'))

print(is_unique_ascii('abcde'))
print(is_unique_ascii('abcdeb'))
