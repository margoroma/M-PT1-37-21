import math

a = int(input ("Значение а: "))
b = int(input ("Значение b: "))
c = int(input ("Значение c: "))

if a != 0:
    print("Решаем уравнение: ")
    if b > 0:
        if c > 0:
            print(f'{a}x**2 - {abs(b)}x - {abs(c)} = 0')
        elif c < 0:
            print(f'{a}x**2 - {abs(b)}x + {abs(c)} = 0')    
        else:
            print(f'{a}x**2 - {abs(b)}x = 0')
    elif b < 0:
        if c > 0:
            print(f'{a}x**2 + {abs(b)}x - {abs(c)} = 0')
        elif c < 0:
            print(f'{a}x**2 + {abs(b)}x + {abs(c)} = 0')    
        else:
            print(f'{a}x**2 + {abs(b)}x = 0')
    else:
        if c > 0:
            print(f'{a}x**2 - {abs(c)} = 0')
        elif c < 0:
            print(f'{a}x**2 + {abs(c)} = 0')    
        else:
            print(f'{a}x**2 = 0')
else:
    print("a!=0, уравнение стало линейным")           


if a != 0:
    if b != 0:
        if c != 0: 
            d = b ** 2 - 4 * a * c
            if d > 0:
                x1 = (-b + math.sqrt(d)) / (2 * a)
                x2 = (-b - math.sqrt(d)) / (2 * a)
                print("x1: ", round(x1, 2), "\nx2: ", round(x2, 2))
            elif d < 0:
                print("Решений нет!") 
            else: 
                print("Всего одно значение x1: ", round(-b / (2 * a), 2))
        else:
            print("x1 всегда = 0\nx2: ", round(b / a, 2)) 
    else:
        if c == 0:
                print ("Всегда x = 0")
        else:
            e = c / a
            if e > 0:
                print("x1: ", round(math.sqrt(e), 2), "\nx2: ", round(- math.sqrt(e), 2))
            elif e == 0:
                print ("x1 всегда = 0")
            else:
                print ("Решений нет")
else: 
    print("")  