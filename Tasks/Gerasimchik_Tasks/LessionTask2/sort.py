simple_list = [10, 5, 7, 4, 11, 9, 15, 1, 0, 126, 8, 25]
for i in range(len(simple_list)):
    small = i
    for a in range(i + 1, len(simple_list)):
        if simple_list[small] > simple_list[a]:
            small = a
    simple_list[i], simple_list[small] = simple_list[small], simple_list[i]
    print(simple_list)
print(simple_list)
