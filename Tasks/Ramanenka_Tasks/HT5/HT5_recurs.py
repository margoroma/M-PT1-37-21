"""Recursive function to calculate the sum of all elements in nested list
"""
def sum_elem_list(lists):
    summa = 0
    for i in lists:
        if type(i) != list:
            summa += i
        else:
            summa += sum_elem_list(i)
    return summa

lista = [1, 2, [2, 4, [[7, 8], 4, 6]]]
print(sum_elem_list(lista))
