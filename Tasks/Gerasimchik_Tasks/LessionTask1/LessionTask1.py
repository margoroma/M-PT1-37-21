import math

print("Решение квадратных уравнений типа ax^2+bx+c=0")
a = int(input('Введите a\n'))
b = int(input('Введите b\n'))
c = int(input('Введите c\n'))
out_a = str(a)
if b < 0:
    out_b = str(b)
else:
    out_b = "+" + str(b)

if c < 0:
    out_c = str(c)
else:
    out_c = "+" + str(c)
print(f'Уравнение {out_a}x^2{out_b}x{out_c}=0')

d = b ** 2 - 4 * a * c
if d < 0:
    print('Дискриминант равен', d)
    print("Дискриминант отрицательный, уравнение решений не имеет")
elif d == 0:
    x = (-b + math.sqrt(d)) / (a * 2)
    print('Дискриминант равен', d)
    print("Дискриминант равен нулю, уравнение имеет одно решение:", x)
else:
    x1 = (-b + math.sqrt(d)) / (a * 2)
    x2 = (-b - math.sqrt(d)) / (a * 2)
    print('Дискриминант равен', d)
    print('Дискриминант положительный, уравнение имеет два решения', x1, x2)
