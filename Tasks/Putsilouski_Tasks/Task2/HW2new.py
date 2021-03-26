# 1-29 - минут....
# 31-39 - минут...
# 30 - половина
# 40-59 - без 20-1 минут
# 00 - часов ровно

from datetime import datetime
def slovami(h_c,m_с):

    chasy = {0: "ноль", 1: 'один', 2: "два", 3: 'три', 4: 'четыре', 5: 'пять',
             6: 'шесть', 7: 'семь', 8: 'восемь', 9: 'девять', 10: "десять", 11: "одинадцать", 12: "двенадцать",
             13: "тринадцать", 14: "четырнадцать", 15: "пятнадцать", 16: "шестнадцать", 17: "семьнадцать",
             18: "весьнадцать", 19: "девятнадцать"}
    chasy_kakogo = {1: 'первого', 2: "второго", 3: 'третьего', 4: 'четвертого', 5: 'пятого',
                    6: 'шестого', 7: 'седьмого', 8: 'восьмого', 9: 'девятого', 10: "десятого",
                    11: "одиннадцатого", 12: "двенадцатого"}
    chasy_konc = {1: "часа", 2: "часов", 3: "час"}
    minuty = {1: "одна", 2: "две", 14: "четырнадцать", 13: "тринадцать"}
    minuty_konc = {1: "минута", 2: "минуты", 3: "минут"}
    konc = {1: "надцать", 2: "дцать", 3: "десят", 4: "надцати"}
    if h_c >= 12: h_c = h_c - 12
    if m_с == 0:
        itog = chasy[h_c] + " "
        if h_c == 1: itog = itog + chasy_konc[3]
        if 1 < h_c < 5:          itog = itog + chasy_konc[1]
        if (h_c >= 5 or h_c == 0): itog = itog + chasy_konc[2]
        itog = itog + " ровно"
    if m_с == 30:
        if h_c == 12:
            itog = "Половина " + chasy_kakogo[1]
        else:
            itog = "Половина " + chasy_kakogo[h_c + 1]
    if 0 < m_с <= 39 and m_с != 30:
        if m_с == 1: itog = minuty[m_с] + " " + minuty_konc[1]
        if m_с == 2: itog = minuty[m_с] + " " + minuty_konc[2]
        if m_с == 3 or m_с == 4: itog = chasy[m_с] + " " + minuty_konc[2]
        if 4 < m_с < 20: itog = chasy[m_с] + " " + minuty_konc[3]
        if m_с == 20: itog = chasy[2] + konc[2] + " " + minuty_konc[3]
        if m_с > 20:
            if int(list(str(m_с))[1]) == 1 or int(list(str(m_с))[1]) == 2:
                itog = chasy[int(m_с // 10)] + konc[2] + " " + minuty[int(list(str(m_с))[1])] + " "
            else:
                itog = chasy[int(m_с // 10)] + konc[2] + " " + chasy[int(list(str(m_с))[1])] + " "
            if set(list(str(m_с))[1]) <= {"2", "3", "4"}:
                itog = itog + minuty_konc[2]
            elif set(list(str(m_с))[1]) <= {"1"}:
                itog = itog + minuty_konc[1]
            else:
                itog = itog + minuty_konc[3]

        if (h_c != 24 and h_c != 12):
            itog = itog + " " + chasy_kakogo[h_c + 1]
        else:itog = itog + " " + chasy_kakogo[1]

    if 39 < m_с <= 59:
        m_с = 60 - m_с
        itog = "без "
        if m_с == 20: itog = itog + "двадцати" + " " + minuty_konc[3]
        if 10 < m_с < 20:itog = itog + chasy[m_с % 10][:-1] + konc[4] + " " + minuty_konc[3]
        if m_с == 10: itog = itog + "десяти" + " " + minuty_konc[3]
        if m_с < 10:
            if set(str(m_с)) <= {"9", "6", "5", "7"}: itog = itog + chasy[m_с][:-1] + "и"
            if set(str(m_с)) <= {"8"}: itog = itog + chasy[m_с][:-3] + "ьми"
            if set(str(m_с)) <= {"4", "3"}: itog = itog + chasy[m_с][:-1] + "ех"
            if m_с == 2: itog = itog + "двух" + " " + minuty_konc[3]
            if m_с == 1: itog = itog + "одной" + " "+ minuty_konc[2]
        itog =itog+ " "+ chasy[h_c+1]
    print(itog)

f_line = input("Введи время,:\n")
s_line = f_line.replace(' ', '')
if ':' not in s_line:
    sys.exit("Неверный формат, начни заново")
t_line = s_line.split(":")
h_с = int(t_line[0])
m_с = int(t_line[1])
if h_с < 0 or h_с > 24 or m_с < 0 or m_с > 59:
    sys.exit("Неверный формат, начни заново")

mnow = datetime.today().minute
hnow = datetime.today().hour
print("Сейчас:", hnow, " часов", mnow, " минут")
h_seichas = int(hnow)
m_seichas = int(mnow)

flag = 0
if flag == 0:
    slovami(h_seichas, m_seichas)
    flag=1
if flag == 1:
    print("Вы ввели следующее")
    slovami(h_с, m_с)
    flag = 0

