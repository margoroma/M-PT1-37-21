import mtmf

vyr = input("выражение\n").replace(" ","")

# (4-3)*(12+(2-1))
for y in range(len(vyr)):
    print(vyr[y])
    if vyr[y] == ")":
        print("нашел")

        for x in range(y, -1, -1):
            print("зашел", vyr[x])
            if vyr[x] == "(":
                print("new", vyr[x])
                pr = vyr[x:y+1]
                print("fdsfsdfdsfsd",pr)
                vyr = vyr.replace(vyr[x:y+1], mtmf.vn(vyr[x:y+1]))
                break
    else:
        continue
