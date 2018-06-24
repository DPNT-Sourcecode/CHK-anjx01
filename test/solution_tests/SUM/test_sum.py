import unittest

from lib.solutions.SUM import sum_solution


class TestSum(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(sum_solution.compute(1, 2), 3)

    def test_sum_string(self):
        with self.assertRaises(TypeError):
            sum_solution.compute(1,'2')

    def test_sum_float(self):
        with self.assertRaises(TypeError):
            sum_solution.compute(1,1.1)

if __name__ == '__main__':
    unittest.main()
