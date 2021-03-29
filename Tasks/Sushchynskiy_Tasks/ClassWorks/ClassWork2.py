a = "thirteen five thirteen five seventeen fourteen fifteen one thirteen fourteen twenty"
b = a.split(" ")

# из члов -> в числа

c = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10, "eleven": 11, 
"twelve": 12, "thirteen": 13, "fourteen": 14, "fifteen": 15, "sixteen": 16, "seventeen": 17, "eighteen": 18, "nineteen": 19, "twenty": 20}

a1 = []
for i in b:
    for j in c:
        if i == j:
            a1.append(c[j])
print(a1)

# исключить дубликаты

a2 = set(a1)
a3 = list(a2)
print(a3)

# сортировка по возрастанию
a3.sort()
print(a3)

# вычисления

a4 = []
for i in range(len(a3)):
    if i < len(a3) - 2:
        a4.append(a3[i] * a3[i + 1])
        a4.append(a3[i + 1] + a3[i + 2])
    else:
        break
print(a4)

# сумма нечетных чисел

print(a4)
a5 = []
for i in a3:
    if i % 2 == 1:
        a5.append(i)

print(sum(a5))