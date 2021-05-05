from decimal import Decimal


def change(money, cost):
    coin = ('2', '1', '0.50', '0.20', '0.10', '0.05', '0.02', '0.01')
    return_string = ''
    you_change = Decimal(money) - Decimal(cost)
    for i in coin:
        if you_change // Decimal(i):
            return_string += f'{you_change // Decimal(i)} x {i}\n'
            you_change = you_change - (you_change // Decimal(i)) * Decimal(i)
    return return_string


print(change('13.20', '3.20'))
