import decimal

decimal.getcontext().prec = 7

def summary(depo,percent,year):

    month = year*12
    perc_per_month = percent/100/12

    for i in range(month):

        per_month = decimal.Decimal(depo)*decimal.Decimal(perc_per_month)
        depo+=per_month


    return depo

def show_my_money(depo):

    print("Сумма вашего депозита равна :",int(depo),"руб.",(round(depo%1*100)),"коп.")


sum = summary(20000, 15, 5)
show_my_money(sum)