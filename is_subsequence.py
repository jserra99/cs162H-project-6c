# Author: Joseph Serra
# GitHub username: jserra99
# Date: 11/2/2023
# Description: Project-6c; Is Subsequence

def is_subsequence(first_string: str, second_string: str):
    """ Returns true if the first string is a subsequent of the second string. """
    if len(first_string) == 0:
        return True
    if len(second_string) == 0:
        return False
    if first_string[-1] == second_string[-1]:
        return is_subsequence(first_string[:-1], second_string[:-1])
    return is_subsequence(first_string, second_string[:-1])
