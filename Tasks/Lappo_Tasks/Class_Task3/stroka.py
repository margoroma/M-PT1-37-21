x = "five thirteen two eleven seventeen two one thirteen ten four eight five nineteen"
numbers = {
"one" : 1 ,
"two" : 2,
"three" : 3,
"four" : 4,
"five" : 5,
"six" : 6,
"seven" : 7,
"eight" : 8,
"nine" : 9,
"ten" : 10,
"eleven" : 11,
"twelve" : 12,
"thirteen" : 13,
"fourteen" : 14,
"fifteen" : 15,
"sixteen" : 16,
"seventeen" : 17,
"eighteen" : 18,
"nineteen" : 19,
"twenty" : 20
}

y = x.split(' ')


a=0
rez=list()

for i in y:
    y2 =str(numbers[y[a]])
    rez.append(y2)
    a+=1

rez=list(set(rez))

rez=list(map(int, rez))




rez2=list()
i=1

while i < len(sorted(rez)):
    c=rez2[i-1]*rez2[i]
    rez2.append(c)
    i+=1


#print(rez)




#for i in y:
#    z=numbers[y[i]]
#    rez.append(z)
#    i+=1

#print(rez)


#y1 = y[0]
#print(y1)

#y2 =str(numbers[y1])
#print(y2)