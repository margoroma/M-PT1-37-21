"""
Сумма элементов вложенных списков

Написать функцию для вычисления суммы всех элементов вложенных списков.
Функция должна быть рекурсивной, то есть она должна обходить каждый элемент 
списка и вызывать саму себя, если текущий элемент так же является списком. 
"""


def sum_nested_lists(lst):
    summa = 0
    for elem in lst:
        if not isinstance(elem, list):
            summa += elem
        else:
            summa += sum_nested_lists(elem)
    return summa


numb_lst = [1, 2, [2, 4, [[7, 8], 4, 6]]]
print(sum_nested_lists(numb_lst))
