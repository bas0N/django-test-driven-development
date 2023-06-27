"""
Sample tests
"""

from django.test import SimpleTestCase
from app import calc


class CalcClass(SimpleTestCase):
    """Test calc class"""
    def test_add_numbers(self):
        """Test calc module"""
        self.assertEqual(calc.add(3, 8), 11)

    def test_substract_numbers(self):
        """Test substract numbers"""
        self.assertEqual(calc.substract(5, 11), 6)
