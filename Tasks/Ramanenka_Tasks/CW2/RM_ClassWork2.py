# Решение линейного уравнения, вводимого пользователем

import numpy as np
import matplotlib.pyplot as plt

l = input('Введите линейное уравнение: ')

m = l.replace(' ','')
k = m.replace('y=', '')
p = k.split('x')

k = int(p[0])
b = int(p[1])

iks = int(input("Введите значение х: "))
igr = k * iks + b
print(f'y = {igr}')
x1 = -b / k
print(f'Корень уравнения: {x1:.3f}')

x = np.linspace(-15, 15, num=50)
y = k * x + b

plt.scatter(x1,0)
plt.plot(x,y,'r-')
plt.grid(True)
plt.title('Линейная функция')
plt.show()

