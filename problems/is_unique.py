# Implement an Algorithm to determine if a srring has all unque characters. What if you can't use additional data structures?


string_a = "abcdefg"
string_b = "hello"
string_c = "abcd e fg"

def is_unique(string):
    char_set = {}
    i = 0
    while i < len(string):
        if char_set[string[i]]:
            return False
        char_set[string[i]] = True
        i += 1
    return True

assert is_unique(string_a) == True
assert is_unique(string_b) == False
assert is_unique(string_c) == False

# Are we using unicode or ASCII?
# Assuming we are using ASCII, the set of possible characters < 128

def is_unique_improved(string):
    if len(string) > 128:
        return False
    char_set = {}
    for i in range(len(string)):
        if char_set[i]:
            return False
        char_set[i] = True
    return True

# If we can't use additional data structures, we could (a) compare every character of the string to every other character of the string => O(n^2) time and O(1) space
# or (b) sort the string, then check for adjacent duplicate characters.