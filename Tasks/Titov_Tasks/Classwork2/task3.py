lst1 = [1, 2, 10]
lst2 = [10, 2, 1]
a = 0
if len(lst1) != len(lst2):
    print("Списки не равны")
else:
    for i in range(len(lst1)):
        if lst1[i] != lst2[i]:
            a = False
            break
        else:
            a = True
    if a:
        print("Списки равны")
    else:
        print("Списки не равны")
