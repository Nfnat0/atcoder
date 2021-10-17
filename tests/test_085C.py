import unittest
from ABC import take_params_085C


class Test_085C(unittest.TestCase):
    def test_normal1(self):
        actual = take_params_085C.main(9, 45000)
        self.assertIn(actual, ['4 0 5', '0 9 0'])

    def test_not_found(self):
        actual = take_params_085C.main(20, 196000)
        self.assertEqual("-1 -1 -1", actual)
