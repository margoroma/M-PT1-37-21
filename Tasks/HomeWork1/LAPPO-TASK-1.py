import math
money = 20000
year = 5
month = 12
per = year*month
perc = 15
rez = money*math.pow((1+15/(12*100)),per)
print(round(rez,2))