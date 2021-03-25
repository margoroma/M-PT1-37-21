# Реализовать текстовый вывод текущего времени + текстовый вывод времени, введённого с консоли.
# Для получения текущего времени использовать модуль datetime.
# 1-29 - минут....
# 31-39 - минут...
# 30 - половина
# 40-59 - без 20-1 минут
# 00 - часов ровно

# ______________Введение времени с терминала______________
# f_line = input("Введи время,:\n")
# s_line = f_line.replace(' ', '')
# if ':' not in s_line:
#     sys.exit("Неверный формат, начни заново")
# t_line = s_line.split(":")
# h_с = int(t_line[0])
# m_с = int(t_line[1])
# if h_с < 0 or h_с > 24 or m_с < 0 or m_с > 59:
#     sys.exit("Неверный формат, начни заново")

from datetime import datetime
ch = {0:"ноль", 1: 'один', 21: 'одна', 2: "два", 22: "две", 3: 'три', 4: 'четыре', 40: "сорок", 5: 'пять',
      6: 'шесть', 7: 'семь', 8: 'восемь', 9: 'девять', 10: "десять", 12: "двенадцать", 11:"одинадцать"}
ch1_n30_39 = {1: 'первого', 2: "второго", 3: 'третьего', 4: 'четвертого', 5: 'пятого',
              6: 'шестого', 7: 'седьмого', 8: 'восьмого', 9: 'девятого', 10: "десятого", 11: "надцатого"}
ok_numbers = {11-19: "надцать", 20-30: "дцать", 50-80: "десят",
              90: "носто", "11-19-2": "надцати"}
ok_word_h = {"standart": "час",
             "am_2-4,21": "а", "am_5-20": "ов"}
ok_word_m = {"standart": "минут", 1: "а",
             2: "ы", 40 : "дцати" }

mnow = datetime.today().minute  #текущее время минуты
hnow = datetime.today().hour  #текущее время часы
print("Сейчас:", hnow," часов", mnow," минут")
h_c = int(hnow)
m_с = int(mnow)


if h_c>12: h_c=h_c-12

if m_с == 0:
            itog = ch[h_c] + " " + ok_word_h["standart"]
            if 1 < h_c < 5:
                itog = itog + ok_word_h["am_2-4,21"]
            if (h_c >= 5 or h_c == 0):
                itog = itog + ok_word_h["am_5-20"]
            itog = itog + " ровно"
if 0 < m_с <= 39 and m_с != 30:  # выбор варианта отображения  1-29 - минут.... пятнадцать минут седьмого
            if m_с == 1: itog = ch[21] + " " + ok_word_m["standart"] + ok_word_m[1]  # 1
            if m_с == 2: itog = ch[22] + " " + ok_word_m["standart"] + ok_word_m[2]  # 2
            if 2 < m_с <= 4: itog = ch[m_с] + " " + ok_word_m["standart"] + ok_word_m[2]  # от 2 до 4
            if 4 < m_с <= 10: itog = ch[m_с] + " " + ok_word_m["standart"]  # от 2 до 4
            if m_с == 11: itog = ch[1] + ok_numbers[11 - 19] + " " + ok_word_m["standart"]  # 11
            if m_с == 12: itog = ch[22] + ok_numbers[11 - 19] + " " + ok_word_m["standart"]  # 12
            if m_с == 13: itog = ch[3] + ok_numbers[11 - 19] + " " + ok_word_m["standart"]  # 13
            if 13 < m_с <= 19: itog = ch[(m_с % 10)][:-1] + ok_numbers[11 - 19] + " " + ok_word_m[
                "standart"]  # от 14 до 19
            if 19 < m_с <= 39:
                itog = ch[int(m_с//10)] + ok_numbers[20-30]
                if (m_с == 21 or m_с == 31):
                    itog = itog + " " + ch[21]  # 21
                    itog = itog + " " + ok_word_m["standart"]+ok_word_m[1]
                if (m_с == 22 or m_с == 32):
                    itog = itog + " " + ch[22]  # 22
                if m_с > 22: itog = itog + " " + ch[int(str(m_с)[1])]  # от 23 до 39
                itog = itog + " " + ok_word_m["standart"]
            itog = itog +" "+ ch1_n30_39[h_c+1]
if m_с == 30:
    if h_c < 10: itog = "Половина " + ch1_n30_39[h_c + 1]
    if h_c == 10: itog = "Половина " + ch[1] + ch1_n30_39[h_c + 1]
    if h_c == 11: itog = "Половина " + ch[22] + ch1_n30_39[h_c]
if 39 < m_с <= 59:
    m_с = 60 - m_с
    itog = "без "
    if m_с == 20: itog = itog + ch[int(str(m_с)[0])] + ok_word_m[40]
    if 20 > m_с > 13: itog = itog + ch[(m_с % 10)][:-1] + ok_numbers[11 - 19 - 2]
    if m_с == 13: itog = itog + ch[(m_с % 10)][:-1] + "и" + ok_numbers[11 - 19 - 2]
    if m_с == 12: itog = itog + ch[(m_с % 10)][:-1] + "е" + ok_numbers[11 - 19 - 2]
    if m_с == 11: itog = itog + ch[(m_с % 10)] + ok_numbers[11 - 19 - 2]
    if 11 > m_с > 8 or 7 > m_с > 4: itog = itog + ch[m_с][:-1] + "и"
    if m_с == 8: itog = itog + ch[m_с][:-3] + "ьми"
    if m_с == 4: itog = itog + ch[m_с] + "х"
    if m_с == 3: itog = itog + ch[m_с][:-1] + "ех"
    if m_с == 2: itog = itog + ch[m_с][:-1] + "ух"
    if m_с == 1: itog = itog + ch[m_с][:-2] + "ной"
    itog = itog + " " + ok_word_m["standart"]
    if h_c <= 9: itog = itog + " " + ch1_n30_39[h_c + 1]
    if h_c == 10: itog = itog + " " + ch[h_c / 10] + ch1_n30_39[11]
    if h_c == 11: itog = itog + " " + ch[22] + ch1_n30_39[11]
    # itog = itog +" " +ch[h_c]

print(itog)









#
#
#
#
# # if m_с == 1:
# #      print(ch["1g"], ok_word_m["standart"] + ok_word_m["1"], ch[7].replace("м", "д")+"ого")
# # if m_с == 2:
# #      print(ch{"2g"})
#
#
#
