import unittest

from lib.solutions.CHK import checkout_solution


class TestHlo(unittest.TestCase):
    def test_multipricing(self):
        self.assertEqual(checkout_solution.checkout(['AAAAAAAA']),330)






    # def test_input_string(self):
    #     with self.assertRaises(TypeError):
    #         hello_solution.hello(1)

    # def test_ret_hlworld(self):
    #     self.assertEqual(hello_solution.hello('John'),"Hello, John!")
if __name__ == '__main__':
    unittest.main()