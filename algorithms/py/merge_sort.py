def merge(array_1, array_2):
    final = []
    i = 0
    j = 0
    while True:
        if i >= len(array_2):
            for k in range(j, len(array_1)):
                final.append(array_1[k])
            break
        
        if j >= len(array_1):
            for l in range(i, len(array_2)):
                final.append(array_2[l])
            break

        if array_2[i] <= array_1[j]:
            final.append(array_2[i])
            i += 1
        else:
            final.append(array_1[j])
            j += 1
    print(final)
    return final

def merge_sort(array):
    if len(array) == 1:
        return array
    left = split(array[0:int(len(array) / 2)])
    right = split(array[int(len(array) / 2):])
    return merge(left, right)