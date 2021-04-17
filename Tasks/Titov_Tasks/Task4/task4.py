"""
Функция get_ranges

Реализовать функцию get_ranges которая получает на вход непустой список
неповторяющихся целых чисел, отсортированных по возрастанию,
которая этот список “сворачивает”.
"""


def get_ranges(lst):
    ranges = ''
    min_index = 0

    for current_index in range(1, len(lst)):
        if lst[current_index] != lst[current_index-1] + 1:
            ranges += f"{_step_range(lst[min_index],lst[current_index-1])}, "
            min_index = current_index
    ranges += _step_range(lst[min_index], lst[current_index])
    return ranges


def _step_range(min_val, max_val):
    if min_val == max_val:
        range_numb = f"{max_val}"
    else:
        range_numb = f"{min_val}-{max_val}"
    return range_numb


numb_lst = [1, 2, 3, 5, 9, 10, 15, 22, 23, 67]
print(get_ranges(numb_lst))
