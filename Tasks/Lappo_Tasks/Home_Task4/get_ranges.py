l1=[0, 1, 2, 3, 4, 7, 8, 10]
l2=[4,7,10]
l3=[2, 3, 8, 9]

def get_ranges(l):
    l.append(9999)
    rezult = ""
    counter = 0
    for i in range (1,len(l)):
        if l[i] != l[i-1]+1:
            if l[counter] == l[i-1]:
                rezult+=str(l[counter]) + " "
                counter = i
            else:
                rezult+=str(l[counter]) + "-"+str(l[i-1]) + " "
                counter = i
    return rezult






print(get_ranges(l1))
print(get_ranges(l2))
print(get_ranges(l3))