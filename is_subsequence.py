# Author: Joseph Serra
# GitHub username: jserra99
# Date: 11/2/2023
# Description: Project-6c; Is Subsequence

def is_subsequence(first_string: str, second_string: str):
    """ Returns true if the first string is a subsequent of the second string. """
    if second_string.lower().find(first_string.lower()) == -1:
        return False
    return True
