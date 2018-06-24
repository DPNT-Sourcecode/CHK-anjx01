import unittest

from lib.solutions.SUM import sum_solution


class TestSum(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(sum_solution.compute(1, 2), 3)

    def test_sum_string(self):
        self.assertEqual(sum_solution.compute(1,'2'), 'x')

if __name__ == '__main__':
    unittest.main()
