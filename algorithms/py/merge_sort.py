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
    return final

print(merge([1,3,5,7,9], [2,4,5,7,8,9]))