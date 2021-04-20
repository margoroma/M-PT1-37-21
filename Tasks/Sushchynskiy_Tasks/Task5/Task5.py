def get_sum(l):
    sum = 0
    for el in l:
        if isinstance(el, int):
            sum += el
        else:
            sum += get_sum(el)
    return sum

l = [1, 2, [2, 4, [9, [7, 8], 4, 6, 1, [1, 2], 1]], 2, [1, 2, 2], 5]

print(get_sum(l))