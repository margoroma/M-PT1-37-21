a = float(20000)
b = int(5)
c = b * 12
d = float(15)
for i in range(c):
    a = round(a*(((d/100)/12)+1), 2)
    print(i + 1, "месяц, сумма:", a)
