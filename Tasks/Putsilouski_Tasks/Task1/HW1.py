# Депозит:
# начальная сумма - 20000 BYN
# срок - 5 лет
# процент - 15%
# ежемесячная капитализация
#
# Вычислить сумму на счету в конце указанного срока.
import math

s = float(input("Введите начальный депозит:\n"))
tl = int(input("Срок депозита, лет:\n"))
tn = tl*12
pr = float(input("Процентная ставка, %:\n"))
for i in range(tn):
    s = round(s*(((pr/100)/12)+1), 2)
    print(i+1, "месяц, сумма:", s)

# ______________________________________________________
# 3x^2-14*x-5=0
a = int(input("введи А\n"))
b = int(input("введи B\n"))
c = int(input("введи C\n"))
ur = str(str(a)+"x^2")

if a == 1 or a == -1:
    ur = str(ur.replace("1", ""))

if b > 0:
    if b == 1:
        ur = ur + "+x"
    else:
        ur = ur+"+"+str(b)+"*x"
else:
    if b == -1:
        ur = ur + "-x"
    else:
        ur = ur + str(b) + "*x"

if c > 0:
    if c == 1:
        ur = ur + "+1"
    else:
        ur = ur+"+"+str(c)
else:
    if c == -1:
        ur = ur + "-1"
    else:
        ur = ur + str(c)
print(ur+"=0")

D = b*b - 4*a*c
if D > 0:
    print("Будет 2 решения:")
    x1 = (-b + math.sqrt(D)) / (2*a)
    x2 = (-b - math.sqrt(D)) / (2*a)
    print(x1, "\n", x2)

elif D == 0:
    print("будет 1 решение")
    x1 = (-b - math.sqrt(D)) / (2*a)
else:
    print("Решений не будет")