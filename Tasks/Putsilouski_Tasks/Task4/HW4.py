
a = input("Список:\n")
a = a.split(",")
for i in range(len(a)):
    a[i]=a[i].replace(" ","")


def get_ranges(*args):
    final = ""

    for i in range(len(a)):
        print()
        y = i
        new_arg = a[i]
        for y in range(len(a)):
            if y == len(a) - 1:
                break
            if int(a[y]) == int(a[y + 1]) - 1:
                continue
            else:
                new_arg = str(new_arg) + "-" + str(a[y])
                final = final + new_arg + ","
                i = y + 1
                print(i)
    print(final)


get_ranges(*a)
