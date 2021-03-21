a = int(input("Введите первое число \n"))
b = int(input("Введите второе число \n"))
c = int(input("Введите третье число \n"))

if b > 0 and c > 0:
    print(a,"x**2", "-", b, "x", "-", c, "= 0")
elif b > 0 and c < 0:
    print(a,"x**2", "-", b, "x", c, "= 0")
elif b < 0 and c > 0:
    print(a,"x**2", b, "x", "-", c, "= 0")
D = (b**2) - (4 * a * c)

if D > 0:
    print("Два решения")
    x1 = (-b + D**0.5) / (2 * a)
    x2 = (-b - D**0.5) / (2 * a)
    print(x1, x2)
elif D == 0: 
    print("Одно решение")
    x1 = (-b + D**0.5) / (2 * a)
    print(x1)
else: 
    print("Отрицательное число")
    x1 = (-b + D**0.5) / (2 * a)
    print(x1)