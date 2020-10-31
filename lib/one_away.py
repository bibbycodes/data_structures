# There are three types of edits that can be performed on a string, insert a char, remove a char or replace a char.
# Given two strings, write a function that checks if they are one edit (or zero edits) away

# EG
    # pale, ple => true
    # pales, pale => true,
    # pale, bale => true,
    # pale, bake => false

# Theory:
#   Firstly, if both strings are identical, we need no edits, return True
#   We can traverse the string to check if at each point, the chars are identical:
#       If not identical, an edit must be made. num_edits += 1
#       If num_edits > 1 return False
#       Else return true
#       If an edit must be made, check next char in other string to see if identical to current char of current string,
#           The pointer must be moved accordingly

# Algorithm:
    # i, j = 0
    # while i < len(string_a) and j < len(string_b)
        # if string_a[i] == string_b[j]:
        # else num_edits += 1
            # if string_a[i + 1] == string_b[j]:
            #    insertion at string a, or deletion in string b => j-- or i ++
            # else:
            #    letter change
        # i, j ++

# Backwards
    # i, j = len(string_a) - 1, len(string_b) - 1
    # while i, j > 0:
    # if string_a[i] != string_b[j]
        # num_edits += 1
        # if string_a[i - 1] == string_b[j]:
            # insertion in string_b at j + 1 or deletion in string_a at i
            # j += 1
        # else letter change
        # i, j --

import unittest

def one_away(string_a, string_b):
    if string_a == string_b:
        return True
    # messy way to account for "" and "b"
    if 0 in [len(string_a), len(string_b)] and 1 in [len(string_a), len(string_b)]:
        return True
    i, j = len(string_a) - 1, len(string_b) - 1
    num_edits = 0
    while i >= 0 or j >= 0:
        if string_a[i] != string_b[j]:
            num_edits += 1
            if string_a[i - 1] == string_b[j]:
                j += 1
        if num_edits > 1:
            return False
        i -= 1
        j -= 1
    return True

assert one_away("pale", "ple") == True
assert one_away("pales", "pale") == True
assert one_away("pale", "bale") == True
assert one_away("pale", "bake") == False
assert one_away("paleabc", "pleabc") == True
assert one_away("a", "b") == True
assert one_away("de", "d") == True
assert one_away("pale", "pale") == True
assert one_away("pse", "pale") == False
assert one_away("pas", "pale") == False
assert one_away("pales", "ples") == True
assert one_away("pkle", "pable") == False
assert one_away("pal", "palkes") == False
assert one_away("", "d") == True