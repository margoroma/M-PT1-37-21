z = input("Введите уравнение:")

z = z.replace(' ', '')
z = z.replace('y=', '')

print(z)
mas=z.split('x')

x=mas[0]

if x=='':
    x=1
else:
    x=int(mas[0])

b=int(mas[1])

x1 = input("Введите Х:")

ur=x*int(x1)+b

print("Y= :", str(ur))
