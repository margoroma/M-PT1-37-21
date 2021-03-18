import math
from decimal import Decimal as D
from decimal import ROUND_HALF_DOWN

"""
P - первоначальная сумма, руб.
s - сложная процентная ставка, доли единицы
n - срок вклада, лет
m - количество расчетных периодов с течение года

"""

P = 20000
s = 0.15
n = 5
m = 12
S_end = 20000 * (1 + D('0.15') / 12) ** (5 * 12)
print("Сумма к выдаче через 5 лет:", S_end.quantize(D("1.00"), ROUND_HALF_DOWN))