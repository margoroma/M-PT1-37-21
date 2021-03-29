a = [1, 2, 3, 4, 5]
b = [1, 2, 7, 4, 5]

if not len(a) == len(b):
    print('Списки отличаются')
else:
    for i in range(len(a)):
        if a[i] == b[i]:
            continue
        print('Списки отличаются')

