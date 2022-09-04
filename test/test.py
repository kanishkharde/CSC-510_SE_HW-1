import unittest

from prime import prime_check
from celsius import convert

class TestReturnValues(unittest.TestCase):
    
    def test_prime(self):
        """
        Test for a known return value
        """
        self.assertEqual(prime_check(5), 120)

    def test_convert(self):
        """
        Test for a known return value
        """
        self.assertEqual(convert(32.5), 34)
