def get_ranges(my_list):

    new_str = ""
    start = my_list[0]
    end = my_list[0]
    my_list.append("")
    for i in range(1, len(my_list)):
        if my_list[i] == end + 1:
            end = my_list[i]
            continue            
        if start == end:
            new_str += str(start) + " "
        else:
            new_str += str(start) + "-" + str(end) + " "    
        start = end = my_list[i]
        str_final = ", ".join(new_str.split())
    return str_final

my_list = [1, 3, 5, 2, 7, 6, 10, 18, 19, 35]
my_list = sorted(my_list)
print(get_ranges(my_list))