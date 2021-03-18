def bank_depo(depo, rate, period):
    rate_mont = rate / 12
    monts = period * 12

    for i in range(monts):
        depo += round(depo * rate_mont / 100, 2)

    return round(depo, 2)


print(bank_depo(20000, 15, 5))
