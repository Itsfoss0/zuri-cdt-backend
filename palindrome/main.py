#!/usr/bin/env python3

"""
Test script with examples of how to use
CasCading Palindrome
"""

from palindromes import CascadingPalindrome

cascading = CascadingPalindrome('hello world')
print(cascading)

cascading = CascadingPalindrome('hi mom')
print(cascading)

multiple_match = CascadingPalindrome('mom dad hello world bob lee')
print(multiple_match)

#catching the error thrown
try:
    palindrome = CascadingPalindrome(1337)
    print(palindrome)
except TypeError:
    print('An exception was thrown')


palindrome = 'hello world'
print(CascadingPalindrome(palindrome))
