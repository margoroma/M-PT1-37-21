from datetime import datetime


def convert_time(time_string):
    hour_lexicon = {
        0: ['первого', 'час'],
        1: ['второго', 'два'],
        2: ['третьего', 'три'],
        3: ['четвертого', 'четыре'],
        4: ['пятого', 'пять'],
        5: ['шестого', 'шесть'],
        6: ['седьмого', 'семь'],
        7: ['восьмого', 'восемь'],
        8: ['девятого', 'девять'],
        9: ['десятого', 'десять'],
        10: ['одиннадцатого', 'одиннадцать'],
        11: ['двенадцатого', 'двенадцать'],
        12: ['первого', 'час'],
        13: ['второго', 'два'],
        14: ['третьего', 'три'],
        15: ['четвертого', 'четыре'],
        16: ['пятого', 'пять'],
        17: ['шестого', 'шесть'],
        18: ['седьмого', 'семь'],
        19: ['восьмого', 'восемь'],
        20: ['девятого', 'девять'],
        21: ['десятого', 'десять'],
        22: ['одиннадцатого', 'одиннадцать'],
        23: ['двенадцатого', 'двенадцать'],
    }

    second_digit_minutes_lexicon = {
        1: 'одна минута',
        2: 'две минуты',
        3: 'три минуты',
        4: 'четыре минуты',
        5: 'пять минут',
        6: 'шесть минут',
        7: 'семь минут',
        8: 'восемь минут',
        9: 'девять минут',
        10: 'десять минут',
        11: 'одиннадцать минут',
        12: 'двенадцать минут',
        13: 'тринадцать минут',
        14: 'четырнадцать минут',
        15: 'пятнадцать минут',
        16: 'шестнадцать минут',
        17: 'семнадцать минут',
        18: 'восемнадцать минут',
        19: 'девятнадцать минут',
        0: 'минут',

    }
    first_digit_minutes_lexicon = {
        2: 'двадцать',
        3: 'тридцать',
    }

    current_time_split = time_string.split(':')
    current_hours = int(current_time_split[0])
    current_minutes = int(current_time_split[1])

    if current_minutes == 30:

        return_string = f'Половина {hour_lexicon[current_hours][0]}'
    elif current_minutes == 0:
        if current_hours == 0:
            return_string = 'В Петропавловске-Камчатском полночь'
        elif current_hours == 12:
            return_string = 'В Петропавловске-Камчатском полдень'
        else:
            if current_hours == 1 or current_hours == 13:
                hours_string = ''
            elif (1 < current_hours < 5) or (13 < current_hours < 17):
                hours_string = 'часа '
            else:
                hours_string = 'часов '
            return_string = f'{str.capitalize(str(hour_lexicon[current_hours - 1][1]))} {hours_string}ровно'
    elif current_minutes > 39:
        a = 60 - current_minutes
        minutes_string = ''
        if 5 <= a < 20:
            minutes_string = second_digit_minutes_lexicon[a]
        elif a == 20:
            minutes_string = first_digit_minutes_lexicon[a // 10]
        else:
            second_digit_a = a % 10
            if second_digit_a == 1:
                minutes_string = 'одной минуты'
            elif second_digit_a == 2:
                minutes_string = 'двух минут'
            elif second_digit_a == 3:
                minutes_string = 'трех минут'
            elif second_digit_a == 4:
                minutes_string = 'четырех минут'
        minutes_string = minutes_string.replace('ь', 'и')
        return_string = f'Без {minutes_string} {hour_lexicon[current_hours][1]}'
    else:
        if current_minutes < 20:
            return_string = f'{str.capitalize(str(second_digit_minutes_lexicon[current_minutes]))} {hour_lexicon[current_hours][0]}'
        else:
            first_digit = current_minutes // 10
            second_digit = current_minutes % 10
            return_string = f'{str.capitalize(str(first_digit_minutes_lexicon[first_digit]))} {second_digit_minutes_lexicon[second_digit]} {hour_lexicon[current_hours][0]}'

    return return_string


current_time = datetime.now()
current_time = current_time.strftime("%H:%M")

print(current_time)
print(convert_time(current_time))
#for i in range(24):
#    print(convert_time(f'{i}:40'))

print(convert_time(input('Введите время в формате ЧЧ:ММ\n')))
