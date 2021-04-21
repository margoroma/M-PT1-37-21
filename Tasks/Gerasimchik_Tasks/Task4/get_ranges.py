def get_ranges(a):
    min_index = 0
    return_string = ''

    def to_string(max_index):
        return str(a[min_index]) if min_index == max_index else str(a[min_index])+'-'+str(a[max_index])

    for i in range(1, len(a)):
        if a[i] - a[i-1] != 1:
            return_string += to_string(i-1) + ', '
            min_index = i
    return_string += to_string(i)

    return return_string


print(get_ranges([0, 1, 2, 3, 4, 7, 8, 10, 15, 17, 18, 50]))
