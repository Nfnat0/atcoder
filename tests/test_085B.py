import unittest
from ABC import take_params_085B


class Test_049C(unittest.TestCase):
    def test_1(self):
        self.assertEqual(3, take_params_085B.main(4, 10, 8, 8, 6))

    def test_2(self):
        self.assertEqual(1, take_params_085B.main(3, 15, 15, 15))
