# Given a string, write a function to check if it is a permutation of a palindrome.
# A palindrome is a word or phrase that is the same forwards as it is backwards.
# A permutation is a re-arrangement of letters.
# The palindrome does not need to be limited to just dictionary words
# You can ignore casing and non-letter characters

# Theory => the word is a palindrome permutation if all letters or all letters but one occur an even number of times
# "Tact Coa" => True because there are 2 T's, 2 C's and 2 A's but only one O, Taco Cat
# "Tacto Coa" => True because there are 2 T's, 2 C's, 2 A's and 2 O's eg Tac ooCat
# "Tacta Cooa" => True because there are 2 T's, 2 C's, 3 A's and 2 O's eg Tacoa ocat
# "Tacta Coa" => False because there are 2 T's, 2 C's, 3 A's and 1 O's
# "Tact Co" => False because there are 2 T's, 2 C's 1 A and 1 o, the a and o will always be in the middle

# Algorithm:
    # Downcase string
    # Strip all white space and non letter chars
    # Count occurances of each letter
    # in loop, Count number of letters that have a count that are odd numbered, if > 1 return False

import re
from collections import defaultdict

def palindrome_permutation(string):
    string = string.lower()
    pattern = re.compile('[^a-zA-Z]')
    string = pattern.sub('', string)
    count = defaultdict(int)

    for i in range(len(string)):
        count[string[i]] += 1
    
    odd_number_occurences_count = 0

    for letter in count.keys():
        if count[letter] % 2 == 1:
            odd_number_occurences_count += 1
        if odd_number_occurences_count > 1:
            return False
    return True

# This algorithm takes 0(n) time, where N is the length of the string

assert palindrome_permutation("Tact Coa") == True
assert palindrome_permutation("Tacta Cooa") == True
assert palindrome_permutation("Tacto Coa") == True
assert palindrome_permutation("Tacta Coa") == False
assert palindrome_permutation("Tact Co") == False