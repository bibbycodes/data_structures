def how_sum(target, nums_array, memo = {}):
    if (target in memo):
        return memo[target]
    if target == 0:
        return []
    if target < 0:
        return None

    for num in nums_array:
        rem = target - num
        result_remainder = how_sum(rem, nums_array, memo)
        if result_remainder is not None:
            result_remainder.append(num)
            memo[target] = result_remainder
            return memo[target]

    memo[target] = None
    return None
    
    
        
print(how_sum(8, [2, 3, 5]))