from datetime import datetime


hours_list = ["один", "два", "три", "четыре", "пять", "шесть", "семь",
       "восемь","девять","жесять","одинадцать","двенадцать",'тринадцать',
       'четырнадцать','пятнадцать','шестнадцать','семнадцать','восемнадцать','девятнадцать']
hours_list_second = ['первого', 'второго', 'третьего', 'четвертого', 'пятого', 'шестого',
      'седьмого','восьмого','девятого','десятого','одиннадцатого','двеннадцатого']
hours_list_third = ['час', 'часа', 'часов']
minutes_list_a = ["десять", "двадцать", "тридцать", "двадцати",
         "десяти"]
minutes_list_b = ['девятнадцати', 'восемнадцати', 'семнадцати',
         'шестнадцати','пятнадцати','четырнадцати',
         'тринадцати','двенадцати',"одиннадцати"]
minutes_list_c = ["одна", "двe", "три", "четыре", "пять", "шесть", "семь",
       "восемь","девять"]
minutes_list_d = ['девяти', 'восьми', 'семи', 'шести',
         'пяти','четырех','трех','двух','одной']

minutes_list_e = ["одинадцать", "двенадцать"]
minutes_list_f = ['минута', 'минуты', 'минут']
noon_night = ['полдень', 'полуночь']



add_time = datetime.strftime(datetime.now(),"%H : %M")

time = add_time.split(":")
my_hours = int(time[0])
my_minutes = int(time[1])

full_min = (my_minutes // 10)
part_min = (my_minutes % 10)


if my_hours == 12 and my_minutes == 0:
    print(noon_night[0])
    exit()
elif my_hours == 24 and my_minutes == 0:
    print(noon_night[1])
    exit()

if my_hours > 12:
    my_hours = my_hours - 12
if my_hours == 1:
    hour_word_itself = hours_list_third[0]
elif my_hours >= 2 and my_hours <= 4:
    hour_word_itself = hours_list_third[1]
else:
    hour_word_itself = hours_list_third[2]

if full_min < 3:

    hour_hour = hours_list[my_hours - 1]

    if part_min >= 2 and part_min <= 4:
        minutes_word_itself = minutes_list_f[1]
    elif part_min == 1:
        minutes_word_itself = minutes_list_f[0]
    else:
        minutes_word_itself = minutes_list_f[2]

    if my_minutes > 0 and my_minutes < 10 :
        min_s = minutes_list_c[part_min - 1]
        print(hour_hour, hour_word_itself, min_s, minutes_word_itself)

    elif my_minutes > 10 and my_minutes < 20:
        slice_min_a = hours_list[10::]
        minutes_list_b = slice_min_a[part_min - 1]
        print(hour_hour, hour_word_itself, minutes_list_b, minutes_word_itself)

    elif full_min == 0 and part_min == 0:
        print(hour_hour, hour_word_itself)
    elif part_min == 0:
        minutes_list_b = minutes_list_a[full_min - 1]
        print(hour_hour, hour_word_itself, minutes_list_b, minutes_word_itself)

    else:
        minutes_list_b = minutes_list_a[full_min - 1]
        min_s = minutes_list_c[part_min - 1]
        print(hour_hour, hour_word_itself, minutes_list_b, min_s, minutes_word_itself)

if full_min == 3 and part_min == 0:
    h_hour = hours_list_second[my_hours]
    print('пол ' + h_hour)

if my_minutes >= 31 and my_minutes <= 59:

    hour_hour = hours_list[my_hours]

    if part_min >= 1 and part_min <= 8 or part_min == 0:
        minutes_word_itself = minutes_list_f[2]
    else:
        minutes_word_itself = minutes_list_f[1]

    if part_min == 0:
        w_m = minutes_list_a[full_min - 1]
        print('без ', w_m, minutes_word_itself, hour_hour)

    if my_minutes >= 31 and my_minutes <= 39:
        if my_hours == 12:
            hour_hour = hours_list_third[0]
        w_m = minutes_list_a[full_min]
        w_mm = minutes_list_d[part_min - 1]
        print('без ', w_m, w_mm, minutes_word_itself, hour_hour)

    elif my_minutes >= 41 and my_minutes <=49:
        w_mm = minutes_list_b[part_min - 1]
        if part_min == 9:
            minutes_word_itself = minutes_list_f[2]
        print('без ', w_mm, minutes_word_itself, hour_hour)
    else:
        w_mm = minutes_list_d[part_min - 1]
        print('без ', w_mm, minutes_word_itself, hour_hour)

