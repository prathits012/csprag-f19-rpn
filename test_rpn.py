import unittest
import rpn
class TestBasics(unittest.TestCase):
    def test_add(self):
        result = rpn.calculate('1 1 +')
        self.assertEqual(2,result)
    def test_sub(self):
        result = rpn.calculate('5 3 -')
        self.assertEqual(2,result)
    def test_badinput(self):
        result = rpn.calculate('5 3 -')
        self.assertEqual(2,result)
    def test_pow(self):
        result = rpn.calculate('3 3 ^')
        self.assertEqual(27,result)
