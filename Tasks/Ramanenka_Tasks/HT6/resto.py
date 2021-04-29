# import decimal

nominal_byn = [0.01, 0.02, 0.05, 0.10, 0.20, 0.50, 1.00, 2.00, 5.00, 10.00, 20.00, 50.00, 100.00, 200.00, 500.00]

# price = float('Enter the price: \n')
price = 3.69
print(f'Price is: {price}')

def short_change(money, byn):
    for i in range(len(byn)):
        if byn[i] > money:
            byn = byn[i:]
            resto = byn[0] - money
            break
    return resto

def short_money(change_to_buyer, byn, list_of_money=[]):

    if len(byn) == 0:
        return list_of_money
    for i in reversed(range(len(byn))):
        if byn[i] < change_to_buyer:
            list_of_money.append(byn[i])
            byn = byn[:i+1]
            change_to_buyer -= byn[i]
            return short_money(change_to_buyer, byn)


change = short_change(price, nominal_byn)
print(f'Change is: {change}')
money_return = short_money(change, nominal_byn)
print(f'Nominals of change: {money_return}')


