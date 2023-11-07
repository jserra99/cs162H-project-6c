# Author: Joseph Serra
# GitHub username: jserra99
# Date: 11/2/2023
# Description: Project-6c; Is Subsequence Tester

import unittest
from is_subsequence import is_subsequence


class IsSubsequenceTester(unittest.TestCase):

    def test_is_subsequence(self):
        """ Test is_subsequence() """
        str_one = "nana"
        str_two = "banana"
        self.assertTrue(is_subsequence(str_one, str_two))
        str_one = "elo"
        str_two = "hello"
        self.assertTrue(is_subsequence(str_one, str_two))
        str_one = "hol"
        str_two = "hello"
        self.assertFalse(is_subsequence(str_one, str_two))
