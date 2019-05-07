import unittest
from src.ComplexNumber import *


class TestComplexNumber(unittest.TestCase):
    def test_add_binomials(self):
        c1 = ComplexNumber.binomial(1, 1)
        c2 = ComplexNumber.binomial(1, 1)
        res = ComplexNumber.binomial(2, 2)
        self.assertEqual(c1 + c2, res)

    def test_sub_binomials(self):
        c1 = ComplexNumber.binomial(1, 1)
        c2 = ComplexNumber.binomial(1, 1)
        res = ComplexNumber.binomial(0, 0)
        self.assertEqual(c1 - c2, res)

    def test_mul_binomials(self):
        c1 = ComplexNumber.binomial(1, 1)
        c2 = ComplexNumber.binomial(1, 1)
        res = ComplexNumber.binomial(0, 2)
        self.assertEqual(c1 * c2, res)

    def test_mul_pi_mult(self):
        c1 = ComplexNumber.polar_with_pi(2, 1)
        c2 = ComplexNumber.polar_with_pi(3, 0)
        res = ComplexNumber.polar_with_pi(6, 1)
        self.assertEqual(c1 * c2, res)

    def test_mul_decimal(self):
        c1 = ComplexNumber.polar_with_decimal(2, pi)
        c2 = ComplexNumber.polar_with_decimal(3, 0)
        res = ComplexNumber.polar_with_decimal(6, pi)
        self.assertEqual(c1 * c2, res)

    def test_mul_pi_mult_with_binomial(self):
        c1 = ComplexNumber.polar_with_pi(1, 1)
        c2 = ComplexNumber.binomial(1, 1)
        res = ComplexNumber.polar_with_pi(sqrt(2).real, 1.25)
        self.assertEqual(c1 * c2, res)

    def test_div_binomials(self):
        c1 = ComplexNumber.binomial(1, 1)
        c2 = ComplexNumber.binomial(1, 1)
        res = ComplexNumber.polar_with_decimal(1, 0)
        self.assertEqual(c1 / c2, res)

    def test_div_pi_mult(self):
        c1 = ComplexNumber.polar_with_pi(1, 1)
        c2 = ComplexNumber.polar_with_pi(2, 0)
        res = ComplexNumber.polar_with_pi(0.5, 1)
        self.assertEqual(c1 / c2, res)

    def test_div_decimal(self):
        c1 = ComplexNumber.polar_with_pi(1, pi)
        c2 = ComplexNumber.polar_with_pi(2, 0)
        res = ComplexNumber.polar_with_pi(0.5, pi)
        self.assertEqual(c1 / c2, res)

    def test_div_pi_mult_with_binomial(self):
        c1 = ComplexNumber.polar_with_pi(1, 1)
        c2 = ComplexNumber.binomial(1, 1)
        res = ComplexNumber.polar_with_pi(1 / sqrt(2).real, 0.75)
        self.assertEqual(c1 / c2, res)

    def test_div_throws_exception(self):
        c1 = ComplexNumber.binomial(1, 1)
        c2 = ComplexNumber.binomial(0, 0)
        self.assertRaises(DivideByZero, lambda: c1 / c2)
