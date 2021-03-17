import math as mt
def earnings_calculator():
    orig_amount = float(input("Введите сумму которую вы бы хотели положить на счёт: "))
    percentage = float(input("Введите годовой процент который вы бы хотели получить: "))
    number_of_years = float(input("Введите количество лет на которое вы бы хотели сделать в клад в годах: "))
    number_of_monts = 12
    final_number = (orig_amount * (1 + (percentage / 100) / number_of_monts) ** (number_of_monts * number_of_years))
    return ("В конце срока счёт будет соствалсять {0}BYN"
            .format(final_number))

print(earnings_calculator())
