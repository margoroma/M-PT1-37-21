"""
Решение квадратного уравнения вида
a*x**2-b*x-c=0

Вводятся коэффициенты уравнеия a, b, c.
Требуется: вывести уравнение, найти его корни.
"""

value_a = input("Input a: ")
value_b = input("Input b: ")
value_c = input("Input c: ")

a, b, c = float(value_a), float(value_b), float(value_c)
sign_b = sign_c = "-"
if b < 0:
    sign_b = "+"
    value_b = str(-b)
if c < 0:
    sign_c = "+"
    value_c = str(-c)

print("Equation: " + value_a + "*x**2" + sign_b + value_b + "*x" + sign_c +
      value_c + "=0", sep="")

if a == 0:
    print("Linear equation. х =", round((c / -b), 2))
else:
    discr = b ** 2 - 4 * a * c
    if discr > 0:
        x1 = (-b + discr ** (1 / 2)) / (2 * a)
        x2 = (-b - discr ** (1 / 2)) / (2 * a)
        print("Discriminant > 0. Roots of equation")
        print("x1 =", round(x1, 2), "\nx2 =", round(x2, 2))
    elif discr == 0:
        x = -b / (2 * a)
        print("Discriminant = 0. One root x =", round(x, 2))
    else:
        print("Discriminant < 0. No roots")
