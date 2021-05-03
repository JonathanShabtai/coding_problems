import unittest
from collections import defaultdict

def urlify(s, num):
    s = s[:num].replace(' ', '%20')
    return s


class Test(unittest.TestCase):
    def test_equal(self):
        self.assertEqual('Mr%20John%20Smith', urlify('Mr John Smith   ', 13))

    """
    dataT = [('abcd'), ('s4fad'), (''), ('adspo')]
    dataF = [('23ds2'), ('hb 627jh=j ()')]

    def test_is_unique(self):
        # true check
        for test_string in self.dataT:
            actual = is_unique(test_string)
            self.assertTrue(actual)
        # false check
        for test_string in self.dataF:
            actual = is_unique(test_string)
            self.assertFalse(actual)
    """


if __name__ == "__main__":
    unittest.main(verbosity=2)
