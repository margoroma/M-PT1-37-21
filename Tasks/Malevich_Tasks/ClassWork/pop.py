import math

dict_num = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10, 'eleven': 11, 'twelve': 12, 'thirteen': 13, 'fourteen': 14, 'fifteen': 15, 'sixteen': 16, 'seventeen': 17, 'eighteen': 18, 'nineteen': 19, 'twenty': 20}
st = 'five thirteen two eleven seventeen two one thirteen ten four eight five nineteen'
s = st.split()
a_num = list()
for x in s:
    #p = dict_num.get(x)
    a_num.append(dict_num[x])
print('Числа: ', a_num)

a_num.sort()
print('Отсортированные числа: ', a_num)
b_num = list(set(a_num))
print('Числа без дублей: ', b_num)

c_num = list()
d_num = list()
for i in range(len(b_num) - 1):
    if i % 2 == 0:
        c_num.append(b_num[i] * b_num[i + 1])
    else:
        d_num.append(b_num[i] + b_num[i + 1])
print('Произведение: ', c_num)
print('Сумма: ', d_num)

sum = 0
for i in range(len(b_num)):
    if b_num[i] % 2 != 0:
        sum += b_num[i]
print('Сумма нечетных: ', sum)


