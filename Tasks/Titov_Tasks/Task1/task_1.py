"""
Формула сложных процентов

Депозит:
начальная сумма - 20000 BYN
срок - 5 лет 
процент - 15%
ежемесячная капитализация
Вычислить сумму на счету в конце указанного срока.
"""

money = 20000
percent = 15
years = 5

money_result = money * (1 + percent / 100 / 12) ** (12 * years)

print("Amount on the account after", years, "years was",
      round(money_result, 2))
