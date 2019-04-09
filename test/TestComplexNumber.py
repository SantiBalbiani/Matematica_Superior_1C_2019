import unittest
from src.ComplexNumber import *


class TestComplexNumber(unittest.TestCase):

    def test_binomial_creation(self):
        cn = ComplexNumber.binomial(1, 3)
        self.assertEqual(cn._saved_as, 1)
        self.assertEqual(cn.real(), 1)
        self.assertEqual(cn.imaginary(), 3)

    def test_pi_creation(self):
        cn = ComplexNumber.polar_with_pi(4, 0.25)
        self.assertEqual(cn._saved_as, 2)
        self.assertEqual(cn.abs(), 4)
        self.assertEqual(cn.pi_mult(), 0.25)

    def test_polar_creation(self):
        cn = ComplexNumber.polar_with_decimal(4, 0.25)
        self.assertEqual(cn._saved_as, 3)
        self.assertEqual(cn.abs(), 4)
        self.assertEqual(cn.phase(), 0.25)
        self.assertIsNone(cn.pi_mult())

    def test_pi_creation_second_positive_round(self):
        cn = ComplexNumber.polar_with_pi(4, 2.25)
        self.assertEqual(cn.abs(), 4)
        self.assertEqual(cn.pi_mult(), 0.25)

    def test_pi_creation_first_negative_round(self):
        cn = ComplexNumber.polar_with_pi(4, -1.75)
        self.assertEqual(cn.abs(), 4)
        self.assertEqual(cn.pi_mult(), 0.25)

    def test_pi_creation_second_negative_round(self):
        cn = ComplexNumber.polar_with_pi(4, -3.75)
        self.assertEqual(cn.abs(), 4)
        self.assertEqual(cn.pi_mult(), 0.25)

    def test_polar_creation_second_positive_round(self):
        cn = ComplexNumber.polar_with_decimal(4, 0.25 + FULL_ROUND)
        self.assertEqual(cn.abs(), 4)
        self.assertEqual(cn.phase(), 0.25)

    def test_polar_creation_first_negative_round(self):
        cn = ComplexNumber.polar_with_decimal(4, 0.25 - FULL_ROUND)
        self.assertEqual(cn.abs(), 4)
        self.assertEqual(cn.phase(), 0.25)

    def test_polar_creation_second_negative_round(self):
        cn = ComplexNumber.polar_with_decimal(4, 0.25 - 2 * FULL_ROUND)
        self.assertEqual(cn.abs(), 4)
        self.assertEqual(cn.phase(), 0.25)

    def test_binomial_to_polar_first_quadrant(self):
        cn = ComplexNumber.binomial(5.40, 8.41)
        self.assertAlmostEqual(cn.abs(), 10, delta=0.1)
        self.assertAlmostEqual(cn.phase(), 1, delta=0.01)
        self.assertIsNone(cn.pi_mult())

    def test_pi_to_binomial_first_quadrant(self):
        cn = ComplexNumber.polar_with_pi(sqrt(2).real, 0.25)
        self.assertAlmostEqual(cn.real(), 1, delta=0.01)
        self.assertAlmostEqual(cn.imaginary(), 1, delta=0.01)

    def test_polar_to_binomial_first_quadrant(self):
        cn = ComplexNumber.polar_with_decimal(10, 1)
        self.assertAlmostEqual(cn.real(), 5.40, delta=0.054)
        self.assertAlmostEqual(cn.imaginary(), 8.41, delta=0.0841)

    def test_binomial_to_polar_fourth_quadrant(self):
        cn = ComplexNumber.binomial(5.40, -8.41)
        self.assertAlmostEqual(cn.abs(), 10, delta=0.1)
        self.assertAlmostEqual(cn.phase(), 5.28, delta=0.01)
        self.assertIsNone(cn.pi_mult())

    def test_pi_to_binomial_fourth_quadrant(self):
        cn = ComplexNumber.polar_with_pi(sqrt(2).real, -0.25)
        self.assertAlmostEqual(cn.real(), 1, delta=0.01)
        self.assertAlmostEqual(cn.imaginary(), -1, delta=0.01)

    def test_polar_to_binomial_fourth_quadrant(self):
        cn = ComplexNumber.polar_with_decimal(10, -1)
        self.assertAlmostEqual(cn.real(), 5.40, delta=0.054)
        self.assertAlmostEqual(cn.imaginary(), -8.41, delta=0.0841)

    def test_binomial_to_polar_second_quadrant(self):
        cn = ComplexNumber.binomial(-5.40, 8.41)
        self.assertAlmostEqual(cn.abs(), 10, delta=0.1)
        self.assertAlmostEqual(cn.phase(), 2.14, delta=0.0214)
        self.assertIsNone(cn.pi_mult())

    def test_pi_to_binomial_second_quadrant(self):
        cn = ComplexNumber.polar_with_pi(sqrt(2).real, 0.75)
        self.assertAlmostEqual(cn.real(), -1, delta=0.01)
        self.assertAlmostEqual(cn.imaginary(), 1, delta=0.01)

    def test_polar_to_binomial_second_quadrant(self):
        cn = ComplexNumber.polar_with_decimal(10, 2.14)
        self.assertAlmostEqual(cn.real(), -5.40, delta=0.054)
        self.assertAlmostEqual(cn.imaginary(), 8.41, delta=0.0841)

    def test_binomial_to_polar_third_quadrant(self):
        cn = ComplexNumber.binomial(-5.40, -8.41)
        self.assertAlmostEqual(cn.abs(), 10, delta=0.1)
        self.assertAlmostEqual(cn.phase(), 4.14, delta=0.0414)
        self.assertIsNone(cn.pi_mult())

    def test_pi_to_binomial_third_quadrant(self):
        cn = ComplexNumber.polar_with_pi(sqrt(2).real, 1.25)
        self.assertAlmostEqual(cn.real(), -1, delta=0.01)
        self.assertAlmostEqual(cn.imaginary(), -1, delta=0.01)

    def test_polar_to_binomial_third_quadrant(self):
        cn = ComplexNumber.polar_with_decimal(10, 4.14)
        self.assertAlmostEqual(cn.real(), -5.40, delta=0.054)
        self.assertAlmostEqual(cn.imaginary(), -8.41, delta=0.0841)

    def test_binomial_string_integer(self):
        cn = ComplexNumber.binomial(1, 3)
        self.assertEqual(str(cn), "(1, 3)")

    def test_binomial_string_float(self):
        cn = ComplexNumber.binomial(1.0, 3.125)
        self.assertEqual(str(cn), "(1.0, 3.125)")

    def test_pi_string(self):
        cn = ComplexNumber.polar_with_pi(1, 0.25)
        self.assertEqual(str(cn), "[1, 0.25π]")

    def test_phase_string(self):
        cn = ComplexNumber.polar_with_decimal(1, 1)
        self.assertEqual(str(cn), "[1, 1]")
