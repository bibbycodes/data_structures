# Assume you have a method sub_string that checks if one string is a substring of another
# Given two strings s1 and s2, write code to check if s2 is a rotation of s1 using only one call to is_substring.
# EG waterbottle is a rotation of erbottlewat

# if s2 is a rotation of s1, s2 will be a substring of s1+s1
from  ds.py.trie import Trie

def is_rotation(s1, s2):
    s1s1 = s1 + s1
    if len(s1) > 0 and len(s1) == len(s2):
        trie = Trie()
        return trie.is_substring(s1s1, s2)

t = Trie()
assert is_rotation("waterbottle", "erbottlewat") == True
            
