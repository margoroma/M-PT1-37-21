spisok=list('9265454231')

rez=list()
i = 0
while i < len(spisok):
    y=min(spisok)
    spisok.remove(y)
    rez.append(y)


print(rez)