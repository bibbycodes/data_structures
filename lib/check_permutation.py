# Given two strings, write a method to decide if one is a permutation of the other
# A Few things to note here, does whitespace count? Should our solution be case sensitive?
# Also Note that strings of different lengths cannot be permutations of each other.


def check_permutation(string_a, string_b):
    if len(string_a) != len(string_b):
        return False
    return sorted(string_a) == sorted(string_b)

# Another solution would be to check if the number of occurances for all characters are the same for both strings
from collections import defaultdict

def check_permutation_2(string_a, string_b):
    char_count = defaultdict(int)
    for char in string_a:
        char_count[char] += 1

    for char in string_b:
        char_count[char] -= 1
        if char_count[char] < 0:
            return False
    return True

assert check_permutation("hello", "elhlo") == True
assert check_permutation("hello", "e lhlo") == False
assert check_permutation("Hello", "elHlo") == True
assert check_permutation("What a nice day it is today", "Its not great out there is it?") == False
assert check_permutation_2("hello", "ehllo") == True
assert check_permutation_2("hello", "e lhlo") == False
assert check_permutation_2("Hello", "elHlo") == True
assert check_permutation_2("Dont Say that", "Say What?") == False

