from random import random

def quick_sort(array, left_index, right_index):
    if left_index < right_index:
        pivot_index = partition(array, left_index, right_index)
        quick_sort(array, left_index, pivot_index - 1)
        quick_sort(array, pivot_index + 1, right_index)

def partition(array, start_index, end_index):
    i = start_index - 1
    pivot_index = end_index
    pivot = array[pivot_index]
    for j in range(start_index, end_index):
        if array[j] <= pivot:
            i += 1
            swap_items(array, i, j)
    swap_items(array, pivot_index, i + 1)
    pivot_index = i + 1
    return pivot_index

def swap_items(array, index_a, index_b):
    temp =  array[index_a]
    array[index_a] = array[index_b]
    array[index_b] = temp

b = [int(random() * 100) for _ in range(100)]
quick_sort(b, 0, len(b) - 1)
print(b)
