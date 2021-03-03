import unittest
from super_algos import find_min, sum_all, find_possible_strings

class MyTestCase(unittest.TestCase):
    def test_find_min(self):
        result = find_min([1, 2, 3, 4])
        self.assertEqual(result, 1)
    def test_find_min_emptylist(self):
        result = find_min([])
        self.assertEqual(result, -1)

    def test_sum_all(self):
        result = sum_all([1, 2, 3, 4, 5])
        self.assertEqual(result, 15)

    def test_find_possible_strings(self):
        result = find_possible_strings(['a', 'b'], 2)
        self.assertEqual(result, ['aa', 'ab', 'ba', 'bb'])

if __name__ == '__main__':
    unittest.main()