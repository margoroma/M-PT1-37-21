z = input("Введите уравнение:")

char1 = '='
char2 = 'x'

per1 = z[z.find(char1)+1 : z.find(char2)]
per1 = per1.replace(' ', '')

per1 = int (per1)

char1 = '+'


per2 = z[z.find(char1)+1 : ]
per2 = per2.replace(' ', '')
per2 = int (per2)

x = input("Введите Х:")

ur=per1*int(x)+per2

print("Y= :", str(ur))

