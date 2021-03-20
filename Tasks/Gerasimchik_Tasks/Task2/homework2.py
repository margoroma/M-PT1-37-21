import datetime


def convert_time(time_string):
    hour_min_lexicon = {
        0: 'первого',
        1: 'второго',
        2: 'третьего',
        3: 'четвертого',
        4: 'пятого',
        5: 'шестого',
        6: 'седьмого',
        7: 'восьмого',
        8: 'девятого',
        9: 'десятого',
        10: 'одиннадцатого',
        11: 'двенадцатого',
        12: 'первого',
        13: 'второго',
        14: 'третьего',
        15: 'четвертого',
        16: 'пятого',
        17: 'шестого',
        18: 'седьмого',
        19: 'восьмого',
        20: 'девятого',
        21: 'десятого',
        22: 'одиннадцатого',
        23: 'двенадцатого',
    }

    hour_max_lexicon = {
        0: 'час',
        1: 'два',
        2: 'три',
        3: 'четыре',
        4: 'пять',
        5: 'шесть',
        6: 'семь',
        7: 'восемь',
        8: 'девять',
        9: 'десять',
        10: 'одиннадцать',
        11: 'двенадцать',
        12: 'час',
        13: 'два',
        14: 'три',
        15: 'четыре',
        16: 'пять',
        17: 'шесть',
        18: 'семь',
        19: 'восемь',
        20: 'девять',
        21: 'десять',
        22: 'одиннадцать',
        23: 'двенадцать',
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
        return_string = f'Половина {hour_min_lexicon[current_hours]}'
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
            return_string = f'{str.capitalize(str(hour_max_lexicon[current_hours - 1]))} {hours_string}ровно'
    elif current_minutes > 34:
        a = 60 - current_minutes
        first_string_minutes = ''
        if 10 <= a < 20:
            minutes_string = second_digit_minutes_lexicon[a]
            minutes_string = minutes_string.replace('ь', 'и')
        else:
            second_digit_a = a % 10
            if a >= 20:
                first_string_minutes = first_digit_minutes_lexicon[a // 10]
                first_string_minutes = first_string_minutes.replace('ь', 'и')
            if second_digit_a > 4:
                minutes_string = second_digit_minutes_lexicon[second_digit_a]
                minutes_string = minutes_string.replace('ь ', 'и ')
            elif second_digit_a == 1:
                minutes_string = 'одной минуты'
            elif second_digit_a == 2:
                minutes_string = 'двух минут'
            elif second_digit_a == 3:
                minutes_string = 'трех минут'
            elif second_digit_a == 4:
                minutes_string = 'четырех минут'
            elif second_digit_a == 0:
                minutes_string = first_string_minutes
            if not a // 10 == 0:
                minutes_string = f'{first_string_minutes} {minutes_string}'
        return_string = f'Без {minutes_string} {hour_max_lexicon[current_hours]}'
    else:
        if current_minutes < 20:
            return_string = f'{str.capitalize(str(second_digit_minutes_lexicon[current_minutes]))} {hour_min_lexicon[current_hours]}'
        else:
            first_digit = current_minutes // 10
            second_digit = current_minutes % 10
            return_string = f'{str.capitalize(str(first_digit_minutes_lexicon[first_digit]))} {second_digit_minutes_lexicon[second_digit]} {hour_min_lexicon[current_hours]}'

    return return_string


current_time = datetime.datetime.now()
current_time = current_time.strftime("%H:%M")

print(current_time)
print(convert_time(current_time))
for i in range(60):
    print(convert_time(f'4:{i}'))
#b = input('Введите время в формате ЧЧ:ММ\n')
#print(convert_time(b))
