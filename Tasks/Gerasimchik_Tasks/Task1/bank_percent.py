from decimal import Decimal, ROUND_FLOOR
def bank_depo(depo, rate, period):
    rate_mont = Decimal(str(rate / 12))
    monts = Decimal(str(period * 12))

    s = Decimal(str(depo)) * ((1 + rate_mont/100) ** monts)
    s = s.quantize(Decimal("1.00"), ROUND_FLOOR)

    return (s)

print(bank_depo(20000, 15, 5))
