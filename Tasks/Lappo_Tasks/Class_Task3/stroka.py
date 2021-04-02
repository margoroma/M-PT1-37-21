x = "five thirteen two eleven seventeen two one thirteen ten four eight five nineteen"

print("Исходная строка: ",x)

numbers = {
"one" : 1 ,
"two" : 2,
"three" : 3,
"four" : 4,
"five" : 5,
"six" : 6,
"seven" : 7,
"eight" : 8,
"nine" : 9,
"ten" : 10,
"eleven" : 11,
"twelve" : 12,
"thirteen" : 13,
"fourteen" : 14,
"fifteen" : 15,
"sixteen" : 16,
"seventeen" : 17,
"eighteen" : 18,
"nineteen" : 19,
"twenty" : 20
}

y = x.split(' ')


a=0

rez=list()

for i in y:
    y2 =str(numbers[y[a]])
    rez.append(y2)
    a+=1

print("В цифры: ",rez)

rez=list(set(rez))

print("Убрали повторы: ",rez)

rez=list(map(int, rez))

print("Перевели в инт: ",rez)

rez=sorted(rez)

print("Посортировали: ",rez)


rez2=list()
rez3=list()
сount=0
i=1

while i < len(sorted(rez)):
    c=rez[i-1]*rez[i]
    
    if c%2:
        сount+=c
        rez3.append(c)

    rez2.append(c)
    i+=1
    if i >= len(sorted(rez)):
        break
    c2=rez[i-1]+rez[i]

    if c2%2:
        сount+=c2
        rez3.append(c2)

    rez2.append(c2)
    i+=1
    if i >= len(sorted(rez)):
        break


print("Перемножили и сложили: ",rez2)
print("Нечетные числа: ",rez3)
print("Сумма нечетных чисел: ",сount)



# rez3=list()
# i=1
# сount=0

# while i <= len(sorted(rez2)):
# #    if rez2[i-1]==int(rez2[i-1]/2)*2: исправил,применил %
#     if rez2[i-1]%2==0:
#         i+=1
#         continue
#     сount+=rez2[i-1]
#     rez3.append(rez2[i-1])
#     i+=1
    
# print("Нечетные числа: ",rez3)
# print("Сумма нечетных чисел: ",сount)