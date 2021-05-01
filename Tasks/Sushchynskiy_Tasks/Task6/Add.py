from decimal import Decimal

coins = ("2", "1", "0.5", "0.2", "0.1", "0.05", "0.02", "0.01")

money = input("Введите цену товра:\n")
banknote = input("Введите сумму оплаты:\n")

change = Decimal(banknote) - Decimal(money)

def get_change(change):
    final_change = ""
    for el in coins:
        if change // Decimal(el):
            final_change += f"{el}: {change // Decimal(el)}\n"
            change -= change // Decimal(el) * Decimal(el)
    return final_change

print(change)
print(get_change(change))