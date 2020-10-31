# Write a method that replaces all whitespace within a string with %20
# You may assume that the string has sufficient space at the end to hold additional characters 
# and that you are given the 'true' length of the string (length of string without additional whitespace)

char_array, true_length = list('Mr John Smith    '), 13

def count_of_characters(string, start, end, target):
    count = 0
    for i in range(start, end):
        char = string[i]
        if string[i] == target:
            count += 1
    return count

def urlify(string, true_length):
    number_of_spaces = count_of_characters(string, 0, true_length, " ")
    new_index = true_length - 1 + (number_of_spaces * 2)
    for i in reversed(range(true_length)):
        if string[i] == " ":
            string[new_index] = '0'
            string[new_index - 1] = '2'
            string[new_index - 2] = '%'
            new_index -= 3
        else:
            string[new_index] = string[i]
            new_index -= 1

urlify(char_array, true_length)
assert char_array == ['M', 'r', '%', '2', '0', 'J', 'o', 'h', 'n', '%', '2', '0', 'S', 'm', 'i', 't', 'h']

