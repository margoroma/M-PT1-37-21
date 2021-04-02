from datetime import datetime

p = input('Введи время в формате HH:MM \n')
t_ent = p.split(':')
h = int(t_ent[0])
m = int(t_ent[1])

a = {0: 'двенадцать', 1: 'один', 2: 'два', 3: 'три', 4: 'четыре', 5: 'пять', 6: 'шесть', 7: 'семь', 8: 'восемь', 9: 'девять', 10: 'десять'}
e = {1: 'второго', 2: 'третьего', 3: 'четвертого', 6: 'седьмого', 7: 'восьмого', 0: 'первого'}
b = {0: 'час', 1: 'минут'}
c = {0: 'а', 1: 'ов', 2: 'ы', 3: 'надцать', 4: 'дцать', 5: 'ого', 6: 'ех', 7: 'ух', 8: 'ой', 9: 'е'}
d = {0: 'половина', 1: 'без четверти', 2: 'без', 3: 'ровно'}

if 0 <= h < 11:
    vr_h = a[h]
elif h == 11:
    vr_h = a[1] + c[3]
elif h == 12:
    vr_h = a[h - 10].replace('а', 'е') + c[3]
elif h == 23:
    vr_h = a[h - 22] + c[3]
elif h == 24:
    vr_h = a[h - 22].replace('а', 'е') + c[3]
else:
    vr_h = a[h - 12]

if m == 1:
    vr_m = a[m].replace('и', '') + c[0]
elif m == 2:
    vr_m = a[m][:-1] + c[9]
elif 2 < m < 11:
    vr_m = a[m]
elif m == 11 or m == 13:
    vr_m = a[m - 10] + c[3]
elif m == 12 or m == 14:
    vr_m = a[m - 10].replace('а', 'е') + c[3]
elif 14 < m < 20:
    vr_m = a[m - 10][:-1] + c[3]
elif m == 20:
    vr_m = a[2] + c[4]
elif m == 21:
    vr_m = a[2] + c[4] + ' ' + a[1].replace('и', '') + c[0]
elif m == 22:
    vr_m = a[2] + c[4] + ' ' + a[2].replace('а', 'е')
elif 22 < m < 30:
    vr_m = a[2] + c[4] + ' ' + a[m - 20]
elif m == 30:
    if h in range (0, 4) or h in range(6, 8):
        vr_m = e[h]
    elif h in range(4, 6) or h in range(8, 10):
        vr_m = a[h + 1][:-1] + c[5]
    elif h == 10:
        vr_m = (a[1] + c[3])[:-1] + c[5]
    elif h == 11:
        vr_m = (a[2].replace('а', 'е') + c[3])[:-1] + c[5]
    elif h in range (12, 16) or h in range(18, 20):
        vr_m = e[h - 12]
    elif h in range(16, 18) or h in range(20, 22):
        vr_m = a[h - 11][:-1] + c[5]
    elif h == 22:
        vr_m = (a[1] + c[3])[:-1] + c[5]
    elif h == 23:
        vr_m = (a[2].replace('а', 'е') + c[3])[:-1] + c[5]
    else:
        vr_m = e[0]
elif m == 31:
    vr_m = a[3] + c[4] + ' ' + a[1].replace('и', '') + c[0]
elif m == 32:
    vr_m = a[3] + c[4] + ' ' + a[2].replace('а', 'е')
elif 32 < m < 40:
    vr_m = a[3] + c[4] + ' ' + a[m - 30]
elif m == 40:
    vr_m = a[2].replace('е', 'а') + c[4].replace('ь', 'и')
elif m in range(41, 45):
    vr_m = a[50 - m][:-1] + c[3].replace('ь', 'и')
elif m == 46:
    vr_m = a[4][:-1] + c[3].replace('ь', 'и')
elif m == 47 or m == 49:
    vr_m = a[50 - m] + c[3].replace('ь', 'и')    
elif m == 48:
    vr_m = a[2].replace('а', 'е') + c[3].replace('ь', 'и')
elif m in range(50, 56) and m != 52:
    vr_m = a[60 - m].replace('ь', 'и')
elif m == 52:
    vr_m = a[8].replace('емь', 'ьми')
elif m in range(56, 58):
    vr_m = a[60 - m][:-1] + c[6]
elif m == 58:
    vr_m = a[2][:-1] + c[7]
elif m == 59:
    vr_m = a[1].replace('и', '') + c[8]


if h == 1 or h == 13:
    nam_h = b[0]
elif h in range(2, 4) or h in range(14, 16):
    nam_h = b[0] + c[0]
else:
    nam_h = b[0] + c[1]


if m in range(0, 40):
    if m % 10 == 1 and m != 11:
        nam_m = b[1] + c[0]
    elif m == 12 or m == 13 or m == 14:
        nam_m = b[1]
    elif m % 10 == 2 or m % 10 == 3 or m % 10 == 4:
        nam_m = b[1] + c[2]
    else:
        nam_m = b[1]
elif m == 59:
    nam_m = b[1] + c[2]
else:
    nam_m = b[1]


if m == 0:
    inp_time = d[3] + ' ' + vr_h + ' ' + nam_h
elif 0 < m < 40 and m != 30:
    inp_time = vr_h + ' ' + nam_h + ' ' + vr_m + ' ' + nam_m
elif m == 30:
    inp_time = d[0] + ' ' + vr_m
elif 39 < m < 60 and m != 45:
    if h == 0 or h == 12 or h == 24:
        inp_time = d[2] + ' ' + vr_m + ' ' + nam_m + ' ' + b[0]
    elif 0 < h < 10:
        inp_time = d[2] + ' ' + vr_m + ' ' + nam_m + ' ' + a[h + 1]
    elif h == 10 or h == 22:
        inp_time = d[2] + ' ' + vr_m + ' ' + nam_m + ' ' + a[1] + c[3]
    elif h == 11 or h == 23:
        inp_time = d[2] + ' ' + vr_m + ' ' + nam_m + ' ' + a[2].replace('а', 'е') + c[3]
    elif 12 < h < 22:
        inp_time = d[2] + ' ' + vr_m + ' ' + nam_m + ' ' + a[h - 11]
elif m == 45:
    if h == 0 or h == 12 or h == 24:
        inp_time = d[1] + ' ' + b[0]
    elif 0 < h < 10:
        inp_time = d[1] + ' ' + a[h + 1]
    elif h == 10 or h == 22:
        inp_time = d[1] + ' ' + a[h + 1]
    elif h == 11 or h == 23:
        inp_time = d[1] + ' ' + a[2].replace('а', 'е') + c[3]
    elif 12 < h < 22:
        inp_time = d[1] + ' ' + a[h - 11]
        
print('Введенное время: ', inp_time)

time_now = datetime.now()
h_now = time_now.hour
m_now = time_now.minute

if 0 <= h_now < 11:
    vr_h_now = a[h_now]
elif h_now == 11:
    vr_h_now = a[1] + c[3]
elif h_now == 12:
    vr_h_now = a[h_now - 10].replace('а', 'е') + c[3]
elif h_now == 23:
    vr_h_now = a[h_now - 22] + c[3]
elif h_now == 24:
    vr_h_now = a[h_now - 22].replace('а', 'е') + c[3]
else:
    vr_h_now = a[h_now - 12]


if m_now == 1:
    vr_m_now = a[m_now].replace('и', '') + c[0]
elif m_now == 2:
    vr_m_now = a[m_now][:-1] + c[9]
if 2 < m_now < 11:
    vr_m_now = a[m_now]
elif m_now == 11 or m_now == 13:
    vr_m_now = a[m_now - 10] + c[3]
elif m_now == 12 or m_now == 14:
    vr_m_now = a[m_now - 10].replace('а', 'е') + c[3]
elif 14 < m_now < 20:
    vr_m_now = a[m_now - 10][:-1] + c[3]
elif m_now == 20:
    vr_m_now = a[2] + c[4]
elif m_now == 21:
    vr_m_now = a[2] + c[4] + ' ' + a[1].replace('и', '') + c[0]
elif m_now == 22:
    vr_m_now = a[2] + c[4] + ' ' + a[2].replace('а', 'е')
elif 22 < m_now < 30:
    vr_m_now = a[2] + c[4] + ' ' + a[m_now - 20]
elif m_now == 30:
    if h_now in range (0, 4) or h_now in range(6, 8):
        vr_m_now = e[h_now]
    elif h_now in range(4, 6) or h_now in range(8, 10):
        vr_m_now = a[h_now + 1][:-1] + c[5]
    elif h_now == 10:
        vr_m_now = (a[1] + c[3])[:-1] + c[5]
    elif h_now == 11:
        vr_m_now = (a[2].replace('а', 'е') + c[3])[:-1] + c[5]
    elif h_now in range (12, 16) or h_now in range(18, 20):
        vr_m_now = e[h_now - 12]
    elif h_now in range(16, 18) or h_now in range(20, 22):
        vr_m_now = a[h_now - 11][:-1] + c[5]
    elif h_now == 22:
        vr_m_now = (a[1] + c[3])[:-1] + c[5]
    elif h_now == 23:
        vr_m_now = (a[2].replace('а', 'е') + c[3])[:-1] + c[5]
    else:
        vr_m_now = e[0]
elif m_now == 31:
    vr_m_now = a[3] + c[4] + ' ' + a[1].replace('и', '') + c[0]
elif m_now == 32:
    vr_m_now = a[3] + c[4] + ' ' + a[2].replace('а', 'е')
elif 32 < m_now < 40:
    vr_m_now = a[3] + c[4] + ' ' + a[m_now - 30]
elif m_now == 40:
    vr_m_now = a[2].replace('е', 'а') + c[4].replace('ь', 'и')
elif m_now in range(41, 45):
    vr_m_now = a[50 - m_now][:-1] + c[3].replace('ь', 'и')
elif m_now == 46:
    vr_m_now = a[4][:-1] + c[3].replace('ь', 'и')
elif m_now == 47 or m_now == 49:
    vr_m_now = a[50 - m_now] + c[3].replace('ь', 'и')    
elif m_now == 48:
    vr_m_now = a[2].replace('а', 'е') + c[3].replace('ь', 'и')
elif m_now in range(50, 56) and m_now != 52:
    vr_m_now = a[60 - m_now].replace('ь', 'и')
elif m_now == 52:
    vr_m_now = a[8].replace('емь', 'ьми')
elif m_now in range(56, 58):
    vr_m_now = a[60 - m_now][:-1] + c[6]
elif m_now == 58:
    vr_m_now = a[2][:-1] + c[7]
elif m_now == 59:
    vr_m_now = a[1].replace('и', '') + c[8]


if h_now == 1 or h_now == 13:
    nam_h_now = b[0]
elif h_now in range(2, 4) or h_now in range(14, 16):
    nam_h_now = b[0] + c[0]
else:
    nam_h_now = b[0] + c[1]


if m_now in range(0, 40):
    if m_now % 10 == 1 and m_now != 11:
        nam_m_now = b[1] + c[0]
    elif m_now == 12 or m_now == 13 or m_now == 14:
        nam_m_now = b[1]
    elif m_now % 10 == 2 or m_now % 10 == 3 or m_now % 10 == 4:
        nam_m_now = b[1] + c[2]
    else:
        nam_m_now = b[1]
elif m_now == 59:
    nam_m_now = b[1] + c[2]
else:
    nam_m_now = b[1]


if m_now == 0:
    time_n = d[3] + ' ' + vr_h_now + ' ' + nam_h_now
elif 0 < m_now < 40 and m_now != 30:
    time_n = vr_h_now + ' ' + nam_h_now + ' ' + vr_m_now + ' ' + nam_m_now
elif m_now == 30:
    time_n = d[0] + ' ' + vr_m_now
elif 39 < m_now < 60 and m_now != 45:
    if h_now == 0 or h_now == 12 or h_now == 24:
        time_n = d[2] + ' ' + vr_m_now + ' ' + nam_m_now + ' ' + b[0]
    elif 0 < h_now < 10:
        time_n = d[2] + ' ' + vr_m_now + ' ' + nam_m_now + ' ' + a[h_now + 1]
    elif h_now == 10 or h_now == 22:
        time_n = d[2] + ' ' + vr_m_now + ' ' + nam_m_now + ' ' + a[1] + c[3]
    elif h_now == 11 or h_now == 23:
        time_n = d[2] + ' ' + vr_m_now + ' ' + nam_m_now + ' ' + a[2].replace('а', 'е') + c[3]
    elif 12 < h_now < 22:
        time_n = d[2] + ' ' + vr_m_now + ' ' + nam_m_now + ' ' + a[h_now - 11]
elif m_now == 45:
    if h_now == 0 or h_now == 12 or h_now == 24:
        time_n = d[1] + ' ' + b[0]
    elif 0 < h_now < 10:
        time_n = d[1] + ' ' + a[h_now + 1]
    elif h_now == 10 or h_now == 22:
        time_n = d[1] + ' ' + a[h_now + 1]
    elif h_now == 11 or h_now == 23:
        time_n = d[1] + ' ' + a[2].replace('а', 'е') + c[3]
    elif 12 < h_now < 22:
        time_n = d[1] + ' ' + a[h_now - 11]

print('Текущее время: ', time_n)