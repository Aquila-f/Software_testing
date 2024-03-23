import unittest
from math import sqrt, exp
from calculator import Calculator

class ApplicationTest(unittest.TestCase):
    def setUp(self):
        self.cal = Calculator()
        self.add_cases = [(1, 2, 3), (0, 0, 0), (-1, 1, 0), (1, -2, -1), (10e5, 10e10, 10e10+10e5)]
        self.divide_cases = [(1, 2), (4, 2), (-1, 1), (1, -1), (10e5, 10e10)]
        self.sqrt_cases = [1, 0, 10e5, 10e10, 10e15]
        self.exp_cases = [2, 0, -1, 1, 10]

    def test_add(self):
        for x, y, expected in self.add_cases:
            with self.subTest(x=x, y=y):
                self.assertEqual(self.cal.add(x, y), expected)
        
        with self.assertRaises(TypeError):
            self.cal.add(1, '2')

    def test_divide(self):
        for x, y in self.divide_cases:
            with self.subTest(x=x, y=y):
                self.assertEqual(self.cal.divide(x, y), x / y)
        
        with self.assertRaises(ZeroDivisionError):
            self.cal.divide(1, 0)
        with self.assertRaises(TypeError):
            self.cal.divide(1, '2')

    def test_sqrt(self):
        for x in self.sqrt_cases:
            with self.subTest(x=x):
                self.assertEqual(self.cal.sqrt(x), sqrt(x))

        with self.assertRaises(ValueError):
            self.cal.sqrt(-1)
    

    def test_exp(self):
        for x in self.exp_cases:
            with self.subTest(x=x):
                self.assertEqual(self.cal.exp(x), exp(x))
        
        with self.assertRaises(TypeError):
            self.cal.exp('2')

if __name__ == '__main__': # pragma: no cover
    unittest.main()
