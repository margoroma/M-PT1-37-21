lst = [1, 2, 3, 4, 6, 7, 13, 18, 25, 26, 19]
lst = sorted(lst)


def get_ranges(l):
    start = l[0]
    stop = l[0]
    line = ""

    for x in l[1:]:
        if stop + 1 == x:
            stop = x
        else:
            if stop == start:
                line += f'{stop}, '
            else:
                line += f'{start}-{stop}, '
            start = x
            stop = x
    if stop == start:
        line += f'{stop}'
    else:
        line += f'{start}-{stop}'

    print(line)


get_ranges(lst)


def fizzbuzz(i):
    while i <= 50:
        if i % 5 == 0 and i % 3 == 0:
            print("FizzBuzz!")
        elif i % 3 == 0:
            print("Fizz!")
        elif i % 5 == 0:
            print("Buzz!")
        else:
            print(i)
        i += 1


fizzbuzz(10)
