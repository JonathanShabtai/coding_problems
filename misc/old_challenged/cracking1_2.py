import numpy as np

def is_perm(string1, string2):
    return sorted(string1) == sorted(string2)


print(is_perm('abc', 'bac'))
print(is_perm('abc', 'abcd'))

def is_perm_hash(string1, string2):
    checker_dict = {}
    for char in string1:
        if char in checker_dict.keys():
            checker_dict[char] += 1
        else:
            checker_dict[char] = 1

    for char in string2:
        if char in checker_dict.keys():
            checker_dict[char] -= 1
        else:
            return False

    return True


print(is_perm_hash('abc', 'bac'))
print(is_perm_hash('abc', 'abcd'))

def is_perm_np(str1, str2):
    answer = np.zeros(128)
    for letter in str1:
        answer[ord(letter)] += 1

    for letter in str2:
        answer[ord(letter)] -= 1

    return np.all(answer == 0)


print(is_perm_np('abc', 'bac'))
print(is_perm_np('abc', 'abcd'))
