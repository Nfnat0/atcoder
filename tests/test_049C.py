import unittest
from ABC import take_params_049C


class Test_049C(unittest.TestCase):
    def test_1(self):
        self.assertEqual("YES", take_params_049C.main('dreamer'))

    def test_2(self):
        self.assertEqual("NO", take_params_049C.main('eraserdrea'))
