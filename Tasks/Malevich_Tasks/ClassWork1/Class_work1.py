import math

print("Решаем квадратное уравнение ax**2 - bx - c = 0")
a = int(input ("Введите значение а:\n"))
b = int(input ("Введите значение b:\n"))
c = int(input ("Введите значение c:\n"))
if a != 0:
    if b != 0:
        if c != 0:
            d = b ** 2 - 4 * a * c
            if d > 0:
                x1 = (-b + math.sqrt(d)) / (2 * a)
                x2 = (-b - math.sqrt(d)) / (2 * a)
                print(d)
                print("Значение 1:\n", round(x1, 2), "\nЗначение 2:\n", round(x2, 2))
            elif d < 0:
                print("Решений нет!") 
            else: 
                x = -b / (2 * a)
                print("Всего одно значение: \n", round(x, 2)) 
        else:
            x1 = 0
            x2 = b / a
            print("Значение 1 всегда равно 0:\n", x1, "\nЗначение 2:\n", round(x2, 2))   
    else:
        if c == 0:
            x = 0
            print ("Всегда одно значение = 0")
        else:
            e = c / a
            if e > 0:
                x1 = math.sqrt(e)
                x2 = - math.sqrt(e)
                print("Значение 1:\n", round(x1, 2), "\nЗначение 2:\n", round(x2, 2))
            elif e == 0:
                print ("Всегда одно значение = 0")
            else:
                print ("Решений нет")
else:
    print("Вы ввели а = 0. Уравнение уже линейное, не квадратное")