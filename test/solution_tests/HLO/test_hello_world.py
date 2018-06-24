import unittest

from lib.solutions.HLO import hello_solution


class TestHlo(unittest.TestCase):
    def test_returns_string(self):
        self.assertEqual(type(hello_solution.hello('abc')),str)

    def test_input_string(self):
        with self.assertRaises(TypeError):
            hello_solution.hello(1)

if __name__ == '__main__':
    unittest.main()