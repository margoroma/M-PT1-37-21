string = "five thirteen two eleven seventeen two one thirteen ten four eight five nineteen"
string = string.split(' ')

#исключение дубликатов:
string = set(string)
string = list(string)
print(string)

#преобразование в цифры:
string = {
    "ten":10,
    "seventeen":17,
    "five":5,
    "two":2,
    "eight":8,
    "nineteen":19,
    "eleven":12,
    "one":1,
    "four":4,
    "thirteen":13,
}
string = string.values()
print(list(string))
string=list(string)


#сортировка по возрастанию:

print(string.sort())

#Долго писать название:
# list4 = []
# for i in range(len(number_list)):
#     if i != len(number_list)-2:
#         list4.append(number_list[i]+number_list[i+1])
#         list4.append(number_list[i+1] * number_list[i+2])
#     else:
#         break
# print(list4)

#сумма всех нечетных чисел:
#s=0
#for i in range(len(number_list)):
#    if number_list[i] % 2 != 0:
#         s+=number_list[i]
#print(s)