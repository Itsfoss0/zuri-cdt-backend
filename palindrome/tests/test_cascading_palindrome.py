#!/usr/bin/env python3

"""
Unittetsts for the CascadingPalindrome class
"""

from unittest import TestCase
from palindromes import CascadingPalindrome


class TestCascadingPalindrome(TestCase):
    """
    Testing class
    """
    def test_matching_palindrome(self):
        self.assertEqual(str(CascadingPalindrome('Hi mom')), 'mom')

    def test_no_matching_palindrome(self):
        self.assertEqual(str(CascadingPalindrome('no match here')), 'None')

    def test_exception_exeptions(self):
        with self.assertRaises(TypeError):
            CascadingPalindrome(1232)
