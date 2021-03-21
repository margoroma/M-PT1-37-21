
def deposit(money, percent, period):
    final_money = money * (1 + percent / (12 * 100)) ** (period * 12)
    return round(final_money, 2)


print(deposit(20000, 15, 5))