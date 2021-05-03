import unittest
import numpy as np
from collections import Counter

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

def is_perm_np(str1, str2):
    answer = np.zeros(128)
    for letter in str1:
        answer[ord(letter)] += 1

    for letter in str2:
        answer[ord(letter)] -= 1

    return np.all(answer == 0)

def is_perm_counter(str1, str2):
    return Counter(str1) == Counter(str2)

class Test(unittest.TestCase):
    dataT = [('abc', 'bac')]
    dataF = [('abc', 'abcd')]

    def test_is_perm(self):
        # true check
        for test_string in self.dataT:
            actual = is_perm(test_string[0], test_string[1])
            self.assertTrue(actual)
        # false check
        for test_string in self.dataF:
            actual = is_perm(test_string[0], test_string[1])
            self.assertFalse(actual)

    def test_is_perm_hash(self):
        # true check
        for test_string in self.dataT:
            actual = is_perm_hash(test_string[0], test_string[1])
            self.assertTrue(actual)
        # false check
        for test_string in self.dataF:
            actual = is_perm_hash(test_string[0], test_string[1])
            self.assertFalse(actual)

    def test_is_perm_np(self):
        # true check
        for test_string in self.dataT:
            actual = is_perm_np(test_string[0], test_string[1])
            self.assertTrue(actual)
        # false check
        for test_string in self.dataF:
            actual = is_perm_np(test_string[0], test_string[1])
            self.assertFalse(actual)

    def test_is_perm_counter(self):
        # true check
        for test_string in self.dataT:
            actual = is_perm_counter(test_string[0], test_string[1])
            self.assertTrue(actual)
        # false check
        for test_string in self.dataF:
            actual = is_perm_counter(test_string[0], test_string[1])
            self.assertFalse(actual)

if __name__ == "__main__":
    unittest.main(verbosity=2)
