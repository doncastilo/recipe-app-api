"""Sample tests
"""
from django.test import SimpleTestCase
from .calc import *
class CalcTests(SimpleTestCase):
    """Test the calc module"""

    def test_add_numbers(self):
        """Test adding numbers together"""
        res = add(5, 6)
        
        self.assertEqual(res, 11)

    def test_substract_numbers(self):
        """Test substracting numbers"""
        res = sustract(5, 6)
        
        self.assertEqual(res, -1)