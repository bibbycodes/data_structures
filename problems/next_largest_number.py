# Create a function that takes a positive integer and returns the next 
# bigger number that can be formed by rearranging its digits.
# https://www.codewars.com/kata/55983863da40caa2c900004e/train/
import math

def next_bigger(number):
    array_of_digits = convert_number_to_array_of_digits_reversed(number)
    j = len(array_of_digits) - 1
    if array_of_digits[j] == 0:
        j -= 1
        
    for i in range(len(array_of_digits)):
        if array_of_digits[i] < array_of_digits[j]:
            swap_items(i, j, array_of_digits)
            return convert_array_of_digits_to_number(array_of_digits)
        
        if array_of_digits[i] == array_of_digits[j]:
            j = i
    return -1


def convert_number_to_array_of_digits_reversed(number):
    array_of_digits = []
    while number > 0:
        number, digit = math.floor(number / 10), number % 10
        array_of_digits.append(digit)
    return array_of_digits

def convert_array_of_digits_to_number(array_of_digits):
    number = 0
    for digit in array_of_digits:
        number = number * 10 + digit
    return number

def swap_items(index_1, index_2, array):
    array[index_1], array[index_2] = array[index_2], array[index_1]

failed = [(9876543210, -1), (1234567890, 1234567908), (937206121, 937206211), (3392506469761, 3392506471669), (10, -1), (121126001641, 121126004116), (315163, 315316)]
for tuple_item in failed:
    print("actual output", next_bigger(tuple_item[0]), "correct output", tuple_item[1], "input", tuple_item[0])
# print(convert_number_to_array_of_digits(123))

