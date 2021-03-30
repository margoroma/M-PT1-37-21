import math

a = input('Input a: ')
b = input('Input b: ')
c = input('Input c: ')
equation = a + '*x*x'
if int(b) < 0:
    equation += b + 'x'
else:
    equation += '+' + b + 'x'
if int(c) < 0:
    equation += c
else:
    equation += '+' + c
equation += '=0'
print(equation)

a = int(a)
b = int(b)
c = int(c)
D = b * b - 4 * a * c
if D > 0:
    print(((-b + math.sqrt(D)) / 2 / a), ((-b - math.sqrt(D)) / 2 / a))
elif D == 0:
    print(-b / 2 / a)
else:
    print('Wrong discriminant')







