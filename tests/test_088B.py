import unittest
from ABC import take_params_088B


class Test_088B(unittest.TestCase):
    def test_normal1(self):
        actual = take_params_088B.main(2, 3, 1)
        self.assertEqual(2, actual)

    def test_normal2(self):
        actual = take_params_088B.main(3, 2, 7, 4)
        self.assertEqual(5, actual)
