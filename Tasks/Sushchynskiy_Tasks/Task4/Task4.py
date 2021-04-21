l = [-56, 4, 5, 6, 8, 9, 10, 12, 13, 14, 16, 17, 20]

def get_ranges(l):
    range_start = l[0]
    range_end = l[0]
    new_l = ""

    for el in l[1:]:
        if range_end + 1 == el:
            range_end = el
        else:
            if range_end == range_start:
                new_l += f"{range_end}, "
            else:
                new_l += f"{range_start}-{range_end}, "
            
            range_start = el
            range_end = el
    if range_end == range_start:
        new_l += f"{range_end}"
    else:
        new_l += f"{range_start}-{range_end}"

    print(new_l)

get_ranges(l)