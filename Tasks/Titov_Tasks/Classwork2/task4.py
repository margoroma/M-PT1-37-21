str_ = "fifteen six ten eight six ten fifteen one four"
numbers = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "eleven",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty"
    }
numb_list = []
for elem in str_.split():
    for k, v in numbers.items():
        if v == elem:
            numb_list.append(k)
print("Замена числами", numb_list)

numb_set = set(numb_list)
print("Без повторов ", numb_set)

numb_list = list(numb_set)
numb_list.sort()
print("Сортированный ", numb_list)

summ = 0
for elem in range(len(numb_list)):
    if numb_list[elem] % 2:
        summ += numb_list[elem]

    if elem == len(numb_list) - 1:
        break
    if not elem % 2:
        mult = (numb_list[elem]) * (numb_list[elem + 1])
        print("Произведение ", elem+1, " и ", elem+2, " равно ", mult)
    else:
        summa = (numb_list[elem]) + (numb_list[elem + 1])
        print("Сумма ", elem+1, " и ", elem+2, " равна ",  summa)

print("Сумма нечетных", summ)
