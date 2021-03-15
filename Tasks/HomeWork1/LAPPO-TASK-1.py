from decimal import Decimal as D
money = D(input('Введите начальную сумму вклада: '))
year = D(input('Введите количество лет вклада: '))
month = D('12')
per = year*month
perc = D(input('Введите процентную ставку вклада: '))
rez = money*((D('1')+perc/(month*D('100')))**per)


print('Вложено     : '+ str(round(money,0)), 'руб.', int((round(money,2)-int(money))*100) , 'коп.')
print('Получено    : '+ str(int(rez)), 'руб.', int((round(rez,2)-int(rez))*100) , 'коп.')
print('Заработано  : '+ str(int(rez-money)), 'руб.', int((round(rez-money,2)-int(rez-money))*100) , 'коп.')

