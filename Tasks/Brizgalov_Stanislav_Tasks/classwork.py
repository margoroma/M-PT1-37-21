l = [9, 5, 8, 3, 4, 1, 7, 2, 6]

for b in l:
    a = True
    while a:
        a = False
        for i in range(len(l) - 1):
            if l[i] > l[i + 1]:
                l[i], l[i + 1] = l[i + 1], l[i]
                a = True

print(l)
