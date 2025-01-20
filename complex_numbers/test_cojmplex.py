import unittest
from complex import Complex

class TestComplex(unittest.TestCase):

    def test_init(self):
        # Test the initialization of the Complex class
        complex_num = Complex(3, 4)
        self.assertEqual(complex_num.re(), 3)
        self.assertEqual(complex_num.im(), 4)

    def test_addition(self):
        # Test addition of two complex numbers
        complex_num1 = Complex(3, 4)
        complex_num2 = Complex(1, 2)
        result = complex_num1 + complex_num2
        self.assertEqual(result.re(), 4)
        self.assertEqual(result.im(), 6)

    def test_subtraction(self):
        # Test subtraction of two complex numbers
        complex_num1 = Complex(3, 4)
        complex_num2 = Complex(1, 2)
        result = complex_num1 - complex_num2
        self.assertEqual(result.re(), 2)
        self.assertEqual(result.im(), 2)

    def test_multiplication(self):
        # Test multiplication of two complex numbers
        complex_num1 = Complex(3, 4)
        complex_num2 = Complex(1, 2)
        result = complex_num1 * complex_num2
        self.assertEqual(result.re(), -5)
        self.assertEqual(result.im(), 10)

    def test_division(self):
        # Test division of two complex numbers
        complex_num1 = Complex(3, 4)
        complex_num2 = Complex(1, 2)
        result = complex_num1 / complex_num2
        self.assertAlmostEqual(result.re(), 2, places=10)
        self.assertAlmostEqual(result.im(), 0, places=10)

    def test_conjugate(self):
        # Test conjugate of a complex number
        complex_num = Complex(3, 4)
        result = complex_num.conjugate()
        self.assertEqual(result.re(), -3)
        self.assertEqual(result.im(), -4)

    def test_str_representation(self):
        # Test the string representation of a complex number
        complex_num = Complex(3, 4)
        self.assertEqual(str(complex_num), '3 + 4i')

    def test_equality(self):
        # Test equality of two complex numbers
        complex_num1 = Complex(3, 4)
        complex_num2 = Complex(3, 4)
        self.assertEqual(complex_num1, complex_num2)

    def test_inequality(self):
        # Test inequality of two complex numbers
        complex_num1 = Complex(3, 4)
        complex_num2 = Complex(1, 2)
        self.assertNotEqual(complex_num1, complex_num2)

if __name__ == '__main__':
    unittest.main()
