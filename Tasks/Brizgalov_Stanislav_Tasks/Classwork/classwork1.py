import math

print('Решаем уравнение ax²-bx-c=0')
a = float(input('Введите значение a: '))
b = float(input('Введите значение b: '))
c = float(input('Введите значение c: '))
d = str(str(a) + "x**2")
if a == 1 or a == -1:
    d = str(d.replace("1", ""))

if b > 0:
    if b == 1:
        d = d + "+x"
    else:
        d = d + "+" + str(b) + "x"
else:
    if b == -1:
        d = d + "-x"
    else:
        d = d + str(b) + "x"
if c > 0:
    if c == 1:
        d = d + "+1"
    else:
        d = d + "+" + str(c)
else:
    if c == -1:
        d = d + "-1"
    else:
        d = d + str(c)
print("Уравнение выглядит так:" '\n' + d + " = 0")
D = b**2 - 4*a*c
print('Дискриминант = ' + str(D))
if D > 0:
    x1 = (-b + math.sqrt(D)) / (2 * a)
    x2 = (-b - math.sqrt(D)) / (2 * a)
    print('x₁ = ' + str(x1))
    print('x₂ = ' + str(x2))
elif D == 0:
    x = -b / (2 * a)
    print('x = ' + str(x))
else:
    print("Корней нет")