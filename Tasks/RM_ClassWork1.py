# Решение квадратного уравнения типа a*x**2-b*x-c=0 с вводимыми целочисленными коэффициентами
import numpy as np
import matplotlib.pyplot as plt

while True:

    a = int(input('Введите число = '))
    b = int(input('Введите число = '))
    c = int(input('Введите число = '))
    x = np.linspace(-15, 15, num=50)

    if b > 0:
        if c > 0:
            print(f'Решаем уравнение {a}*x**2-{abs(b)}*x-{abs(c)}=0')
            y = a*x**2-b*x-c
        else:
            print('Решаем уравнение {}*x**2-{}*x+{}=0'.format(a,abs(b),abs(c)))
            y = (a*(x**2))-abs(b)*x+abs(c)
    else:
        if c > 0:
            print('Решаем уравнение {}*x**2+{}*x-{}=0'.format(a,abs(b),abs(c)))
            y = (a*(x**2))+abs(b)*x-abs(c)
        else:
            print(f'Решаем уравнение {a}*x**2+{abs(b)}*x+{abs(c)}=0')   
            y = (a*(x**2))+abs(b)*x+abs(c)
            
    D = (-b)**2 - 4*a*(-c)
    print(f'Дискриминант равен {D:.2f}')
    
    if D == 0:
        x3 = -(-b) / (2*a)
        print(f'Уравнение имеет 1 корень, равный {x3:.2f}')
    elif D>0:
        x1 = (-(-b) + (D**0.5))/(2*a)
        x2 = (-(-b) - (D**0.5))/(2*a)
        print(f'Уравнение имеет 2 корня, равные {x1:.2f} и {x2:.2f}')
    else:
        print('Уравнение не имеет корней, так как дискриминант отрицателен')

    
    plt.scatter(x1,0)
    plt.scatter(x2,0)
    plt.plot(x,y,'r-')
    plt.grid(True)
    plt.title('Квадратичная функция')
    plt.savefig("equat.png", dpi=400)
    plt.clf()
    print('Желаете ввести новые числа? y/n')
  
    quest = input('')
    if quest == 'n':
        print('Спасибо')
        break
    elif quest == 'y':
        True
    else:
        print('Запустите программу заново, если хотите продолжить')
        break
             