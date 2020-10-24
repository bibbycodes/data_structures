# Implement a methid ti perform basic string compression using the counts of repeated characters. 
# For example, the tring aabcccccaaa would become a2b1c5a3. 
# If the compressed string would not become smaller than the original string, your method dhould return the original string.
# You may assume the string will only contain uppercase and lower case characters (a-zA-Z)

# Algorithm:
    # Iterate through string
    # i = 0
    # while i < len(string)
        # if string[i + 1] = string[i]
            # char_count += 1
        # else
            # new_string.append(string[i])
            # new string.append(char_count)
            # char count = 0
        # i += 1
    # if len(string) <= len(new_string):
        # return string
    # return new_string

def string_compression(string):
    i = 0
    char_count = 0
    new_string = ""
    while i < len(string):
        char_count += 1
        if i + 1 >= len(string) or string[i] != string[i + 1]:
            new_string += (string[i] + str(char_count))
            char_count = 0
        i += 1

    if len(string) <= len(new_string):
        return string
    return new_string

assert string_compression("abcde") == "abcde"
assert string_compression("aabcccccaaa") == "a2b1c5a3"