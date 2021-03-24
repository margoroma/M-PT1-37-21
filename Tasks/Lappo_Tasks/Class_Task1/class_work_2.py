z = input("Введите уравнение:")

char1 = '='
char2 = 'x'

per1 = z.replace(' ', '')
per1 = per1[per1.find(char1)+1 : per1.find(char2)]

if per1 == '':
    per1=1

char1 = 'x'


per2 = z[z.find(char1)+1 : ]
per2 = per2.replace(' ', '')
per2 = int (per2)

x = input("Введите Х:")

ur=per1*int(x)+per2

print("Y= :", str(ur))

