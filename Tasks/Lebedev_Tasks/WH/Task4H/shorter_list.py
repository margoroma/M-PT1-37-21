# 1.Реализовать функцию get_ranges которая получает на вход непустой список неповторяющихся целых чисел,
# отсортированных по возрастанию, которая этот список “сворачивает”.

# get_ranges([0, 1, 2, 3, 4, 7, 8, 10])  ->  "0-4, 7-8, 10"
# get_ranges([4,7,10])  -> "4, 7, 10"
# get_ranges([2, 3, 8, 9])  -> "2-3, 8-9"



def get_ranges(l):
    l.sort()
    string = ""
    start = l[0]
    local_end = l[0]
    for number in l[1:]:
        if number == local_end + 1:
            local_end = number
        else:
            if start == local_end:
                string += f"{local_end},"
            else:
                string += f"{start}-{local_end},"
            start = number
            local_end = number
    if start != local_end:
        string += f"{start}-{local_end},"
    else:
        string += f"{local_end}"
    return string



l=[1,7,2,8,9,13,14,16]


print(get_ranges(l))