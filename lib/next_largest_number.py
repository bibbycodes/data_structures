# Create a function that takes a positive integer and returns the next 
# bigger number that can be formed by rearranging its digits.
# https://www.codewars.com/kata/55983863da40caa2c900004e/train/
import math

def next_bigger(number):
    array_of_digits = convert_number_to_array_of_digits(number)
    pivot_index = find_pivot_index(array_of_digits)
    if pivot_index != None:
        successor_index = find_successor_index(array_of_digits[pivot_index], array_of_digits)
        swap_items(pivot_index, successor_index, array_of_digits)
        left_side = array_of_digits[:pivot_index + 1]
        right_side = array_of_digits[pivot_index + 1:]
        return convert_array_of_digits_to_number(left_side + sorted(right_side))
    return -1

def find_pivot_index(array_of_digits):
    for i in reversed(range(len(array_of_digits))):
        if i == 0:
            break
        if array_of_digits[i] > array_of_digits[i - 1]:
            return i - 1

def find_successor_index(number, array_of_digits):
    for i in reversed(range(len(array_of_digits))):
        if i == 0:
            break
        if array_of_digits[i] > number:
            return i

def convert_number_to_array_of_digits(number):
    array_of_digits = []
    while number > 0:
        number, digit = math.floor(number / 10), number % 10
        array_of_digits.append(digit)
    return list(reversed(array_of_digits))

def convert_array_of_digits_to_number(array_of_digits):
    number = 0
    for digit in array_of_digits:
        number = number * 10 + digit
    return number

def swap_items(index_1, index_2, array):
    array[index_1], array[index_2] = array[index_2], array[index_1]

