import unittest

from lib.solutions.CHK import checkout_solution


class TestHlo(unittest.TestCase):
    def test_1(self):
        self.assertEqual(checkout_solution.checkout(['AAAAAAAA']),330)
    def test_2(self):
        self.assertEqual(checkout_solution.checkout('BEE'),80)

    def test_3(self):
        self.assertEqual(checkout_solution.checkout('FFF'),20)

    def test_4(self):
        self.assertEqual(checkout_solution.checkout('NNNM'),120)

    def test_5(self):
        self.assertEqual(checkout_solution.checkout('HHHHHHHHHH'),80)

    def test_6(self):
        self.assertEqual(checkout_solution.checkout('SSTTXXYYZZ'),45*3+17)







    # def test_input_string(self):
    #     with self.assertRaises(TypeError):
    #         hello_solution.hello(1)

    # def test_ret_hlworld(self):
    #     self.assertEqual(hello_solution.hello('John'),"Hello, John!")
if __name__ == '__main__':
    unittest.main()
