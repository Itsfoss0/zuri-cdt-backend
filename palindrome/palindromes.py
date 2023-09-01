#!/usr/bin/env python3

"""
Determine a cascading palindrome
"""

from typing import Union


class CascadingPalindrome:
    """
    This class is used to determine
    a cascading palindrome. The argument
    during instantiation will be validated against
    the palindrome nature rules implemented herein
    """

    @staticmethod
    def _is_palindrome(value: str) -> bool:
        """
        Determine if a string is a palindrome,
        should only be used inside of this class
        Args:
            value (str): string to check
        Returns:
            returns a boolean
        -----------------------------------
        Example:
            is_pal: bool = _is_palindrome('mom') # True
            is_pal_false: bool = _is_palindrome('zuri') # False
        """
        return value == value[::-1]

    @staticmethod
    def _extract_palindromes(input_string: str) -> Union[str, None]:
        """
        Extract palindromes from an input string
        Should only be used in this class as well
        Args:
            input_string (str): space delimited string
        Returns:
            space delimited palindromes from the input string
            if there's any, else returns None
        -----------------------------------------------------
        Example:
            names = "john doe mom dad and bob lee"
            matched_pals = CascadingPalindrome._extract_palindromes(names)
        """
        if not isinstance(input_string, str):
            raise TypeError('Expected string to be passed')
        words = input_string.split()
        palindromes = []
        for i in range(len(words)):
            for j in range(i + 1, len(words) + 1):
                substring = " ".join(words[i:j])
                if CascadingPalindrome._is_palindrome(substring):
                    palindromes.append(substring)

        return " ".join(palindromes) if palindromes else None

    def __init__(self, input_string: str):
        """
        The constructor
        """
        try:
            self.cas_pal = self.__class__._extract_palindromes(input_string)
        except TypeError:
            raise TypeError()

    def __repr__(self):
        return f'{self.cas_pal}'

    def __str__(self):
        return f"{self.cas_pal}"
