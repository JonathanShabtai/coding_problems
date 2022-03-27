# Check if a string is a permutation of a palindrome
import numpy as np
from itertools import permutations

# bit vector solution
def bit_solution(string_input):
    bit_vector = np.zeros(25)
    for letter in string_input.lower().replace(' ', ''):
        location_letter = ord(letter) - ord('a')
        if bit_vector[location_letter] == 0:
            bit_vector[location_letter] = 1
        else:
            bit_vector[location_letter] = 0
    return sum(bit_vector) <= 1

    # doing a bitwise and on the binary number and the binary number-1:
    # if 0 then either we have a single 1 (00010000-1 & 00010000 = 00001111 & 00010000 = 0)
    # all 0s will work the same (00000-1 & 00000 = 11111 & 00000 = 0)

    # num = int(''.join(str(int(x)) for x in bit_vector), 2)
    # return not(num & (num-1))


print(bit_solution('Tact Coa'))
print(bit_solution('aabbccew'))

# Brute force method (factorial run-time!)
def is_palindrome(input_string):
    return input_string.replace(' ', '') == input_string[::-1].replace(' ', '')

def get_perm(input_string):
    perms = []
    for p in list(permutations(input_string.lower())):
        perms.append(''.join(p))
    return perms

def checker(input_string):
    answers = []
    flag = False
    all_perms = get_perm(input_string)
    for p in all_perms:
        if is_palindrome(p):
            flag = True
            answers.append(p)

    return flag, answers[:2] + ['...']


# print(checker('Tact Coa'))
