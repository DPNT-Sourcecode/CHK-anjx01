import unittest

from lib.solutions.CHK import checkout_solution


class TestHlo(unittest.TestCase):
    def test_multipricing(self):
        self.assertEqual(checkout_solution.checkout('AAA'),130)

    def test_multiitems(self):
        self.assertEqual(checkout_solution.checkout('ABCA'),150)

    def test_int(self):
        self.assertEqual(checkout_solution.checkout(123), -1)
    
    def test_list(self):
        self.assertEqual(checkout_solution.checkout(['A']),-1)



    # def test_input_string(self):
    #     with self.assertRaises(TypeError):
    #         hello_solution.hello(1)

    # def test_ret_hlworld(self):
    #     self.assertEqual(hello_solution.hello('John'),"Hello, John!")
if __name__ == '__main__':
    unittest.main()
