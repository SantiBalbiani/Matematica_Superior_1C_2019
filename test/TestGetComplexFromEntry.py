import unittest
from src.ToComplex import *


class TestGetComplexFromEntry(unittest.TestCase):

    def test_correct_binomial_of_ints(self):
        self.set_complex("(1,2)")
        self.assertEqual(self.complex.real(), 1)
        self.assertEqual(self.complex.imag(), 2)

    def test_correct_binomial_of_floats(self):
        self.set_complex("(1.45,2.95)")
        self.assertEqual(self.complex.real(), 1.45)
        self.assertEqual(self.complex.imag(), 2.95)

    def test_correct_polar_of_ints(self):
        self.set_complex("[1,1]")
        self.assertEqual(self.complex.abs(), 1)
        self.assertEqual(self.complex.phase(), 1)

    def test_correct_polar_of_floats(self):
        self.set_complex("[1.2343,0.23]")
        self.assertEqual(self.complex.abs(), 1.2343)
        self.assertEqual(self.complex.phase(), 0.23)

    def test_correct_pi_of_ints(self):
        self.set_complex("[1, 1Pi]")
        self.assertEqual(self.complex.abs(), 1)
        self.assertEqual(self.complex.phase(), 1)

    def test_correct_pi_of_floats(self):
        self.set_complex("[4.25, 0.25Pi]")
        self.assertEqual(self.complex.abs(), 4.25)
        self.assertEqual(self.complex.phase(), 0.25)

    def set_complex(self, string):
        self.complex = to_complex(string)
