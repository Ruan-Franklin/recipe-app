"""
Sample tests
"""

from django.test import SimpleTestCase

from app import calc


class CalcTests(SimpleTestCase):
    """Tests for the calc module"""

    def test_add_numbers(self):
        """Test adding numbers together"""
        res = calc.add(5, 6)

        self.assertEqual(res, 11)

    def test_subtract_numbers(self):
        """Test subtracting numbers together"""
        res = calc.subtract(10, 5)
        self.assertEqual(res, 5)

    def test_multiply_numbers(self):
        """Test multiplying numbers together"""
        res = calc.multiply(5, 3)
        self.assertEqual(res, 15)

    def test_divide_numbers(self):
        """Test dividing numbers together"""
        res = calc.divide(10, 2)
        self.assertEqual(res, 5)
