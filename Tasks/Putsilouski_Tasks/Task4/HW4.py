a = input("Список:\n")
a = a.split(",")
for i in range(len(a)):
    a[i] = a[i].replace(" ", "")
n = 0  # начало отсчета для вызову ф
y = len(a)
print("Длинна спика:", y)

def get_ranges(n, y, *args):
    global final
    if n == 0:
        final = str(a[n])
    else:
        final = final + "," + str(a[n])
    if n == y - 1:
        return (final)
    for i in range(n, y):
        if i == y - 1:
            final = final + "-" + a[y - 1]
            return (final)
        if int(a[i]) == int(a[i + 1]) - 1:
            continue
        else:
            if i == n:
                n = i + 1
                get_ranges(n, y, *args)
                return (final)
            else:
                final = final + "-" + a[i]
                n = i + 1
                get_ranges(n, y, *args)
                return (final)


print(get_ranges(n, y, *a))
