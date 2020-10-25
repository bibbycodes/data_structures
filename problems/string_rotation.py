# Assume you have a method sub_string that checks if one string is a substring of another
# Given two strings s1 and s2, write code to check if s2 is a rotation of s1 using only one call to is_substring.
# EG waterbottle is a rotation of erbottlewat

# Algorithm:
    # Take first char of s1
    # Find index of char in s2
    # slice s2 at index
    # s2 = second_half + first_half
    # if is_substring(s1,s2) return true

from  ds.py.trie import Trie

def is_rotation(s1, s2):
    first_char = s1[0]
    index = find_slice_index(s2, first_char)
    if index:
        s2 = s2[index:] + s2[:index]
        trie = Trie()
        if trie.is_prefix(s1,s2):
            return True
    return False

def find_slice_index(word, first_char):
    for i in range(len(word)):
        if word[i] == first_char:
            return i
    return False

assert is_rotation("waterbottle", "erbottlewat") == True
            
