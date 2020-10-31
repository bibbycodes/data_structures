def merge(left_array, right_array):
    final = []
    i = j = 0
    while i < len(right_array) and j < len(left_array):
        if right_array[i] <= left_array[j]:
            final.append(right_array[i])
            i += 1
        else:
            final.append(left_array[j])
            j += 1

    for k in range(j, len(left_array)):
        final.append(left_array[k])
        
    for l in range(i, len(right_array)):
        final.append(right_array[l])
    return final

def merge_sort(array):
    if len(array) == 1:
        return array
    left = merge_sort(array[0:len(array) // 2])
    right = merge_sort(array[len(array) // 2:])
    return merge(left, right)

if __name__ == '__main__':
    from random import random
    array = [int(random() * 1000) for _ in range(1000)]
    print(merge_sort(array))

