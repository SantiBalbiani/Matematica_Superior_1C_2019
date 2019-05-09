import unittest
from src.ComplexNumber import *


class TestComplexNumber(unittest.TestCase):
    def test_3_th_root_of_imaginary_binomial(self):
        c = ComplexNumber.binomial(0, -8)
        n = 3
        answ = c.n_th_root(n)
        res = [ComplexNumber.polar_with_decimal(2, 0.5*pi),
               ComplexNumber.polar_with_decimal(2, 7/6*pi),
               ComplexNumber.polar_with_decimal(2, 11/6*pi)]
        for i in range(n):
            self.assertEqual(answ[i].abs(), res[i].abs())
            self.assertAlmostEqual(answ[i].phase(), res[i].phase(), delta=0.01)

    def test_3_th_root_of_imaginary_with_pi(self):
        c = ComplexNumber.polar_with_pi(8, 1.5)
        n = 3
        res = [ComplexNumber.polar_with_pi(2, 0.5),
               ComplexNumber.polar_with_pi(2, 7/6),
               ComplexNumber.polar_with_pi(2, 11/6)]
        self.assertEqual(c.n_th_root(n), res)

    def test_3_th_root_of_imaginary_with_decimal(self):
        c = ComplexNumber.polar_with_decimal(8, 1.5*pi)
        n = 3
        answ = c.n_th_root(n)
        res = [ComplexNumber.polar_with_decimal(2, 0.5*pi),
               ComplexNumber.polar_with_decimal(2, 7/6*pi),
               ComplexNumber.polar_with_decimal(2, 11/6*pi)]
        for i in range(n):
            self.assertEqual(answ[i].abs(), res[i].abs())
            self.assertAlmostEqual(answ[i].phase(), res[i].phase(), delta=0.01)

    def test_4_th_root_of_unity(self):
        primitives = ComplexNumber.roots_of_unity(4, True)
        res = [ComplexNumber.polar_with_pi(1, 0.5), ComplexNumber.polar_with_pi(1, 1.5)]
        self.assertEqual(primitives, res)



