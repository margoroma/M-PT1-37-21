from decimal import Decimal as D
import math

a = D(input('Введите А: '))
b = D(input('Введите B: '))
c = D(input('Введите C: '))

plus='+'
minus='-'

if D(b)<0:
    bm=b*(-1)
    b1= minus+str(bm)
else:
    b1=plus+str(b)

if D(c)<0:
    cm=c*(-1)
    c1=minus+str(cm)
else:
    c1=plus+str(c)

1

print('Вы ввели коэфициенты:',  "A =", a,  "B =", b1,  "C =", c1)
print('Полученное квадратное уравнение:' , str(a)+'x*x'+str(b1)+'x'+str(c1)+'=0')

Disc=b**2-4*a*c
print('Дискриминант D =',Disc)

if Disc>0:

    x1 = (-D(b) + D(math.sqrt(Disc))) / (D('2')*D(a))
    х2 = (-D(b) - D(math.sqrt(Disc))) / (D('2')*D(a))
    print('x1=', x1)
    print('x1=', х2)

elif Disc == 0:

    x = -b / (2 * a)
    print('x= ', x)

else:

    print("Корней нет")