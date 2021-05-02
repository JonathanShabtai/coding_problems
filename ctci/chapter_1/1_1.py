import unittest
from collections import defaultdict

def is_unique(s):
    char_dict = defaultdict(int)
    for char in s:
        char_dict[char] += 1

    """
    for i in char_dict.values():
        if i > 1:
            return False
    
    return True
    """
    return list(char_dict.values()) == [1 for _ in range(len(char_dict.values()))]

def is_unique_bitvector(s):
    checker = 0
    for char in s:
        value_position = ord(char) - ord('a')
        if (checker & (1 << value_position)) > 0:
            return False
        else:
            checker |= (1 << value_position)
    return True

class Test(unittest.TestCase):
    dataT = [('abcd'), ('s4fad'), (''), ('adspo')]
    dataF = [('23ds2'), ('hb 627jh=j ()')]

    dataT_bitvector = [('abcd'), ('gspdcx')]
    dataF_bitvector = [('aba'), ('bcedscb')]

    def test_is_unique(self):
        # true check
        for test_string in self.dataT:
            actual = is_unique(test_string)
            self.assertTrue(actual)
        # false check
        for test_string in self.dataF:
            actual = is_unique(test_string)
            self.assertFalse(actual)

    def test_is_unique_bitvector(self):
        # true check
        for test_string in self.dataT_bitvector:
            actual = is_unique_bitvector(test_string)
            self.assertTrue(actual)
        # false check
        for test_string in self.dataF_bitvector:
            actual = is_unique_bitvector(test_string)
            self.assertFalse(actual)


if __name__ == "__main__":
    unittest.main(verbosity=2)
