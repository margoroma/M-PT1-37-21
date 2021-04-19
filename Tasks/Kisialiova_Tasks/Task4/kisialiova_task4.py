def get_string(some_list):
    if len(some_list) == 1:
        return str(some_list[0])
    else:
        return f'{some_list[0]}-{some_list[-1]}'


def get_ranges(int_list):
    if len(int_list) == 0:
        return ''
    final_list = []
    temp_list = []
    for i, num in enumerate(int_list):
        if i == 0:
            temp_list.append(num)
            continue
        elif num - 1 == int_list[i-1]:
            temp_list.append(num)
        else:
            final_list.append(get_string(temp_list))
            temp_list.clear()
            temp_list.append(num)
    final_list.append(get_string(temp_list))
    result_string = ', '.join(final_list)
    return result_string


if __name__ == '__main__':
    result = get_ranges([1, 2, 3, 5, 7, 9, 10])
    print(result)
