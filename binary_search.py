array = list(range(666))

# get midpoint
# if target at midpoint index, return array[midpoint]
# else target < array[midpoint], repeat with left half

def binary_search(target, array, start_index, end_index):
    if (end_index - start_index) + 1 <= 0:
        return False
    else:
        mid_point = int(start_index + (end_index - start_index) / 2)
        if array[mid_point] == target:
            return mid_point
        if target < array[mid_point]:
            return binary_search(target, array, start_index, mid_point - 1)
        if target > array[mid_point]:
            return binary_search(target, array, mid_point + 1, end_index)