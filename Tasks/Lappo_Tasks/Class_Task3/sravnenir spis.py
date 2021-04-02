x = [1,2,3]
y = [1,2,3]
z=0
rez=0

if len(x)!=len(y):
    print("Не равны")
else:
    while z<len(x):
        if x[z]==y[z]:
            rez+=1
        z+=1

if len(x)==rez:
    print("Равны")
else:
    print("Не равны")

