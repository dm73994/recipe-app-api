"""
Sample tests
"""

from django.test import SimpleTestCase
from app import calc


class ClacTest(SimpleTestCase):
    """TEST THE CALC MODULE"""

    def test_add_numbers(self):
        """Test adding numbers"""
        res = calc.add(6, 5)
        self.assertEqual(res, 11)

    def test_subtract_numbers(self):
        """Test subtracting numbers."""
        res = calc.subtract(10, 15)

        self.assertEqual(res, 5)
