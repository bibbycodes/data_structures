def can_sum(target, nums_array, cache = {}):
    if target in cache:
        return cache[target]
    if target == 0:
        return True
    if target < 0:
        return False
    for num in nums_array:
        if can_sum(target - num, nums_array) == True:
            cache[target] = True
            return True
    cache[target] = False
    return False

# print(can_sum(7, [4, 3 ]))
# print(can_sum(7, [5, 3, 4, 7, 3 ]))
# print(can_sum(300, [7, 14]))
# print(can_sum(7, [4, 3]))