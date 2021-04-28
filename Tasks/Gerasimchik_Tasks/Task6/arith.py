from decimal import Decimal


def add(a, b):
    return Decimal(a) + Decimal(b)


def sub(a, b):
    return Decimal(a) - Decimal(b)


def mult(a, b):
    return Decimal(a) * Decimal(b)


def div(a, b):
    return Decimal(a) / Decimal(b)
