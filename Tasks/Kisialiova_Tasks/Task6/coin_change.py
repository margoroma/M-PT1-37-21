from decimal import Decimal
coins = ('2', '1', '0.5', '0.2', '0.1', '0.05', '0.02', '0.01')


def coin_change(money, cost):
    result_string = ''
    delivery_money = Decimal(money) - Decimal(cost)
    for i in coins:
        if delivery_money // Decimal(i):
            result_string += f'{delivery_money // Decimal(i)} - {i}\n'
            delivery_money = delivery_money - (delivery_money // Decimal(i)) * Decimal(i)
    return result_string


print(coin_change('10.0', '5.40'))
