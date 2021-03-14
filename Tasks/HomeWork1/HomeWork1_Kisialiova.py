money = 20000

for i in range(0, 60):
    money += money * 0.15 / 12
    i += 1
print(round(money, 2))
