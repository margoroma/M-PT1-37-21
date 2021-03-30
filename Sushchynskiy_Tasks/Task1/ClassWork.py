import math as m
b = int(input("Введите число b: "))
a = int(input("Введите число a: "))
c = int(input("Введите число c: "))

d = b ** 2 - 4 * a * c

q = str(-b) + str(-c)
if b == c == 0:
    print(str(a) + "*x*x" + "-" + str(b) + "*x" + "-" + str(c) + " = 0")
elif a == b == 0:
    print(str(a) + "*x*x" + "-" + str(b) + "*x" + "-" + str(c) + " = 0")
elif a == c == 0:
    print(str(a) + "*x*x" + "-" + str(b) + "*x" + "-" + str(c) + " = 0")
elif a == b == c == 0:
    print(str(a) + "*x*x" + "-" + str(b) + "*x" + "-" + str(c) + " = 0")
elif q.isdigit():
    print(str(a) + "*x*x" + "+" + str(-b) + "*x" + "+" + str(-c) + " = 0")
elif c < 0:
    print(str(a) + "*x*x" + "-" + str(b) + "*x" + "+" + str(-c) + " = 0")
elif b < 0:
    print(str(a) + "*x*x" + "+" + str(-b) + "*x" + "-" + str(c) + " = 0")
else:
    print(str(a) + "*x*x" + "-" + str(b) + "*x" + "-" + str(c) + " = 0")


if a == 0:
    print("Деление на ноль!")
elif d > 0:
    print((-b + m.sqrt(d)) / (2 * a))
    print((-b - m.sqrt(d)) / (2 * a))
elif d == 0:
    print(-b / (2 * a))
else:
    print("Нет решений!")