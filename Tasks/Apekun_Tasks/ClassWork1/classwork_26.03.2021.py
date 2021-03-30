# сравнение массивов
# l = [1,2,3]
# m = [1,2,3]
# if len(l) == len(m):
#     for i in range(len(l)):
#         if l[i] == m[i]:
#             continue
#         else:
#             print(l[i], "!=",m[i])
#             exit()
#     print("list ok")
# else:
#     print("list length incorect")
# бесконечный цикл
# l = [1]
# for x in l:
#     l.append(x+1)
#     print(x)


l = "five thirteen two eleven seventeen two one thirteen ten four eigth five ninehteen"
l2 = [5,13,2,11,17,2,1,13,10,4,8,5,19]
l = l.split()

if len(l) == len(l2):
    # # преобразованние в числа
    for i in range(len(l)):
        l[i] = int(l2[i])
    print(l)
    #
    # # исклбючение дубликатов
    print(set(l))
    #
    # # сортировка массива
    for i in range(len (l)):
        min = i
        for j in range(i+1, len(l)):
            if l[min] > l[j]:
                min = j
            l[i] ,l[min] = l[min],l[i]

    print(l)

    # # вывести значения.....
    for i in range (len(l)-1):
        if i % 2 == 0:
            print(l[i]*l[i+1],end=",")
        else:
            print(l[i]+l[i+1],end=",")

    print("\n")
    # # сумма всех нечетных чисел
    #
    a = 0
    for i in range(len(l)):
        if l[i] % 2 == 1:
            a+=l[i]
    print(a)

else:
    print("list range incorrect")

