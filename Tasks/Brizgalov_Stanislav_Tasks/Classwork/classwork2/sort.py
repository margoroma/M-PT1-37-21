def selection_sort(lst):
    for x in range(len(lst)):
        b = x
        for c in range(x, len(lst)):
            if lst[b] > lst[c]:
                b = c
        lst[x], lst[b] = lst[b], lst[x]
    return lst


lst = [6, 4, 8, 1, 7]
result = selection_sort(lst)
print(result)
