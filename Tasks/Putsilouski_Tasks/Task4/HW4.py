
# a = input("Список:\n")

a = "0, 1, 2, 3, 4, 7, 8, 10"
a = a.split(",")
for i in range(len(a)):
    a[i]=a[i].replace(" ","")
n=0
y=len(a)
print("Длинна спика:", y)
z=1



def get_ranges(n,y,z,*args):

    print("Проход:",z)

    global final

    if n==0:
        final = str(a[n])

    else:
        final = final+","+str(a[n])

    if n == y - 1:
        return (final)


    for i in range(n, y):

        if i == y - 1:  #проверка на последний элемент
            final = final + "-" + a[n+1]
            return (final)

        if int(a[i])==int(a[i + 1]) - 1: continue #проверка на последовательный

        else:  #НЕ подходит
            if i==n: #final==a[i]:
                n = i + 1
                z = z + 1
                get_ranges(n, y, z, *args)
                return (final)
            else:
                final=final +"-"+ a[i]
                n = i + 1
                z = z + 1
                get_ranges(n, y, z, *args)
                return (final)






print(get_ranges(n, y,z, *a))








    # for i in range(len(a)):
    #     print()
    #     y = i
    #     new_arg = a[i]
    #     for y in range(len(a)):
    #         if y == len(a) - 1:
    #             break
    #         if int(a[y]) == int(a[y + 1]) - 1:
    #             continue
    #         else:
    #             new_arg = str(new_arg) + "-" + str(a[y])
    #             final = final + new_arg + ","
    #             i = y + 1
    #             print(i)
    # print(final)

