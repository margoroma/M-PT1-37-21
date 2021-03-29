"""
Текстовый вывод времени

Реализовать текстовый вывод текущего времени +
текстовый вывод времени, введённого с консоли.
Для получения текущего времени использовать модуль datetime.
"""

from datetime import datetime


def time_string(time):
    hours_dict = {
        0: "Полночь",
        1: ["первого", "час"],
        2: ["второго", "два"],
        3: ["третьего", "три"],
        4: ["четвертого", "четыре"],
        5: ["пятого", "пять"],
        6: ["шестого", "шесть"],
        7: ["седьмого", "семь"],
        8: ["восьмого", "восемь"],
        9: ["девятого", "девять"],
        10: ["десятого", "десять"],
        11: ["одиннадцатого", "одиннадцать"],
        12: ["двенадцатого", "двенадцать"],
        13: ["первого", "час"]
    }

    min_dict = {
        0: "минут ",
        1: "одна минута ",
        2: "две минуты ",
        3: "три минуты ",
        4: "четыре минуты ",
        5: "пять минут ",
        7: "семь минут ",
        6: "шесть минут ",
        8: "восемь минут ",
        9: "девять минут ",
        10: "десять минут ",
        11: "одиннадцать минут ",
        12: "двенадцать минут ",
        13: "тринадцать минут ",
        14: "четырнадцать минут ",
        15: "пятнадцать минут ",
        16: "шестнадцать минут ",
        17: "семнадцать минут ",
        18: "восемнадцать минут ",
        19: "девятнадцать минут "
    }
    tens_min_dict = {
        20: "двадцать ",
        30: "тридцать "
    }

    time_str = ""
    hours = int(time.split(':')[0])
    minutes = int(time.split(':')[1])

    if hours > 12:
        hours -= 12

    if minutes == 0:
        if hours == 0:
            time_str = str(hours_dict[hours])
        else:
            if hours == 1:
                hours_end = ""
            elif (hours >= 2) and (hours <= 4):
                hours_end = " часа"
            else:
                hours_end = " часов"
            time_str = str(hours_dict[hours][1]) + f"{hours_end} ровно"

    elif minutes == 30:
        time_str = "Половина " + str(hours_dict[hours + 1][0])

    elif (minutes > 0) and (minutes < 40):
        if minutes < 20:
            minutes_before_40 = str(min_dict[minutes])
        else:
            tens_minutes = minutes // 10 * 10
            minutes -= tens_minutes
            minutes_before_40 = "{0}{1}".format(
                str(tens_min_dict[tens_minutes]), str(min_dict[minutes]))
        time_str = f"{minutes_before_40}" + str(hours_dict[hours + 1][0])

    elif (minutes >= 40) and (minutes < 60):
        minutes = 60 - minutes
        if minutes == 1:
            minutes_after_40 = "одной минуты "
        elif minutes == 2:
            minutes_after_40 = "двух минут "
        elif minutes == 3:
            minutes_after_40 = "трех минут "
        elif minutes == 4:
            minutes_after_40 = "четырех минут "
        elif minutes == 20:
            minutes_after_40 = "двадцати минут "
        else:
            minutes_after_40 = str(min_dict[minutes].replace("ь", "и"))
        time_str = f"Без {minutes_after_40}" + str(hours_dict[hours + 1][1])

    return time_str


time_mod = datetime.now().strftime("%H:%M")
print("Время модуля Datetime")
print(time_mod)
print(time_string(time_mod))

print("\nВремя пользователя")
time_user = input('Введите время в формате ЧЧ:ММ\n')
hours_user = int(time_user.split(':')[0])
minutes_user = int(time_user.split(':')[1])

if (hours_user >= 24) or (minutes_user > 59):
    print("Неверные значения времени")
else:
    print(time_string(time_user))
