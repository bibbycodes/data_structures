# Implement an Algorithm to determine if a srring has all unque characters. What if you can't use additional data structures?
from collections import defaultdict

string_a = "abcdefg"
string_b = "hello"
string_c = "abcd e fg"

def is_unique(string):
    string = string.replace(" ", "")
    cache = defaultdict(int)
    i = 0
    while i < len(string):
        cache[string[i]] += 1
        if cache[string[i]] > 1:
            return False
        i += 1
    return True

assert is_unique(string_a) == True
assert is_unique(string_b) == False
assert is_unique(string_c) == True