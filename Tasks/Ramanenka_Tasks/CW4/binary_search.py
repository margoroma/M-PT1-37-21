from random import randint

def binary_search(list_sort, num):
    mini = 0
    maxi = len(list_sort) - 1
    while mini <= maxi:
        center = (mini + maxi) // 2
        if list_sort[center] == num:
            return center
        elif list_sort[center] > num:
            maxi = center - 1
        elif list_sort[center] < num:
            mini = center + 1
    return (f'No such number')

key = randint(0,20)
lista = [randint(0,20) for x in range(10)]
lista = sorted(lista)
print(f'List is: {lista}')
print(f'Number to search: {key}')
print(f'Result: {binary_search(lista, key)}')