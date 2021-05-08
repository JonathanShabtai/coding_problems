import unittest

def insertion_sort(A):
    for j in range(1, len(A)):
        key = A[j]
        i = j-1
        while i >= 0 and A[i] > key:
            A[i+1] = A[i]
            i -= 1
        A[i+1] = key
    return A

"""
# if no return
A = [5, 2, 4, 6, 1, 3]
insertion_sort(A)
print(A)

"""
class Test(unittest.TestCase):
    data = [([5, 2, 4, 6, 1, 3], [1, 2, 3, 4, 5, 6]), ([1, 2, 1, 2], [1, 1, 2, 2])]

    def test_sort(self):
        # true check
        for test_tuple in self.data:
            ans = insertion_sort(test_tuple[0])
            self.assertEqual(ans, test_tuple[1])

if __name__ == "__main__":
    unittest.main(verbosity=2)
