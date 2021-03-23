import datetime

nmb_dict = {
    1: {
        'hour': {
            'numeral': 'первого',
            'normal': 'час'
        },
        'minute': {
            'normal': 'одна',
            'last': 'одной'
        }
    },
    2: {
        'hour': {
            'numeral': 'второго',
            'normal': 'два'
        },
        'minute': {
            'normal': 'две',
            'last': 'двух'
        }
    },
    3: {
        'hour': {
            'numeral': 'третьего',
            'normal': 'три'
        },
        'minute': {
            'normal': 'три',
            'last': 'трёх'
        }
    },
    4: {
        'hour': {
            'numeral': 'четвёртого',
            'normal': 'четыре'
        },
        'minute': {
            'normal': 'четыре',
            'last': 'четырёх'
        }
    },
    5: {
        'hour': {
            'numeral': 'пятого',
            'normal': 'пять'
        },
        'minute': {
            'normal': 'пять',
            'last': 'пяти'
        }
    },
    6: {
        'hour': {
            'numeral': 'шестого',
            'normal': 'шесть'
        },
        'minute': {
            'normal': 'шесть',
            'last': 'шести'
        }
    },
    7: {
        'hour': {
            'numeral': 'седьмого',
            'normal': 'семь'
        },
        'minute': {
            'normal': 'семь',
            'last': 'семи'
        }
    },
    8: {
        'hour': {
            'numeral': 'восьмого',
            'normal': 'восемь'
        },
        'minute': {
            'normal': 'восемь',
            'last': 'восьми'
        }
    },
    9: {
        'hour': {
            'numeral': 'девятого',
            'normal': 'девять'
        },
        'minute': {
            'normal': 'девять',
            'last': 'девяти'
        }
    },
    10: {
        'hour': {
            'numeral': 'десятого',
            'normal': 'десять'
        },
        'minute': {
            'normal': 'десять',
            'last': 'десяти'
        }
    },
    11: {
        'hour': {
            'numeral': 'одиннадцатого',
            'normal': 'одиннадцать'
        },
        'minute': {
            'normal': 'одиннадцать',
            'last': 'одиннадцати'
        }
    },
    12: {
        'hour': {
            'numeral': 'двенадцатого',
            'normal': 'двенадцать'
        },
        'minute': {
            'normal': 'двенадцать',
            'last': 'двенадцати'
        }
    },
    13: {
        'minute': {
            'normal': 'тринадцать',
            'last': 'тринадцати'
        }
    },
    14: {
        'minute': {
            'normal': 'четырнадцать',
            'last': 'четырнадцати'
        }
    },
    15: {
        'minute': {
            'normal': 'пятнадцать',
            'last': 'пятнадцати'
        }
    },
    16: {
        'minute': {
            'normal': 'шестнадцать',
            'last': 'шестнадцати'
        }
    },
    17: {
        'minute': {
            'normal': 'семнадцать',
            'last': 'семнадцати'
        }
    },
    18: {
        'minute': {
            'normal': 'восемнадцать',
            'last': 'восемнадцати'
        }
    },
    19: {
        'minute': {
            'normal': 'девятнадцать',
            'last': 'девятнадцати'
        }
    },
    20: {
        'minute': {
            'normal': 'двадцать',
            'last': 'двадцати'
        }
    },
    30: {
        'minute': {
            'normal': 'тридцать'
        }
    }
}


def parse_minute(minute_str):
    minute = int(minute_str)
    if minute == 0:
        return ''
    elif minute == 30:
        return 'половина'
    elif minute < 40:
        if minute < 20:
            result_minute_string = get_1_19_minute_string(minute)
        else:
            result_minute_string = get_20_39_minute_string(minute)
        min_str = get_normal_minute_word(minute)
    else:
        result_minute_string = get_40_59_minute_string(minute)
        min_str = get_last_minute_word(minute_str)
    return f'{result_minute_string} {min_str}'


def parse_hour(hour_str, minute_str):
    minute = int(minute_str)
    hour = int(hour_str)
    converted_hour = hour % 12
    current_hour = converted_hour + 1
    if converted_hour == 0:
        converted_hour = 12
    if current_hour == 0:
        current_hour = 12
    if minute == 0:
        result_string = nmb_dict[converted_hour]['hour']['normal']
        hour_word = get_hour_word(converted_hour)
        if hour_word:
            result_string = f'{result_string} {hour_word}'
    elif minute < 40:
        result_string = nmb_dict[current_hour]['hour']['numeral']

    else:
        result_string = nmb_dict[current_hour]['hour']['normal']
    return result_string


def get_40_59_minute_string(minute):
    minute = 60 - minute
    return f"без {nmb_dict[minute]['minute']['last']}"


def get_1_19_minute_string(minute):
    return nmb_dict[minute]['minute']['normal']


def get_20_39_minute_string(minute):
    words = []
    if minute // 10 == 2:
        first_word = nmb_dict[20]['minute']['normal']
    elif minute // 10 == 3:
        first_word = nmb_dict[30]['minute']['normal']
    else:
        first_word = ''
    if first_word:
        words.append(first_word)
    minute = minute % 10
    if minute > 0:
        last_word = nmb_dict[minute]['minute']['normal']
    else:
        last_word = ''
    if last_word:
        words.append(last_word)
    return ' '.join(words)


def get_normal_minute_word(minute):
    if minute % 10 == 1 and minute != 11:
        return 'минута'
    elif minute % 10 in (2, 3, 4) and minute not in (12, 13, 14):
        return 'минуты'
    else:
        return 'минут'


def get_last_minute_word(minute):
    if minute == 1:
        return 'минуты'
    else:
        return 'минут'


def get_hour_word(hour):
    if hour == 1:
        return ''
    elif hour < 5:
        return 'часа'
    else:
        return 'часов'


def get_result_string(result_minute_string, result_hour_string):
    if result_minute_string:
        return f'{result_minute_string} {result_hour_string}'
    else:
        return f'{result_hour_string} ровно'


def convert_time_to_words(hours, minutes):
    minute_str = parse_minute(minutes)
    hour_str = parse_hour(hours, minutes)
    result = get_result_string(minute_str, hour_str)
    return result


if __name__ == '__main__':
    while True:
        time_string = input('Введите время в формате HH:MM, где HH - количество часов, MM - количество минут: ')
        time_string = time_string.strip()
        if ':' in time_string:
            time_split = time_string.split(':')
            hour_string = time_split[0]
            minute_string = time_split[1]
            if 0 <= int(hour_string) < 24 and 0 <= int(minute_string) < 60:
                break
        print('Введен неверный формат времени!')

    result1 = convert_time_to_words(hour_string, minute_string)
    print(result1)

    now = datetime.datetime.now()
    hour_string = str(now.hour)
    minute_string = str(now.minute)
    result2 = convert_time_to_words(hour_string, minute_string)
    print(f'Текущее время: {result2}')
