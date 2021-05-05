
pr ="9+5*5"

def um_dl(x, y,z ):
    if z == "*":
        return int((int(x) * int(y)))
    else:
        return int((int(x) / int(y)))

def su_rz (x,y,z):
    if z == "+":
        return int((int(x) + int(y)))
    else:
        return int((int(x) - int(y)))

def vn(pr):
    result=list(pr)
    print(pr)
    while result.count("*") or result.count("/"):
        for i in range(len(result)):
            print(i)
            if result[i]=="*" or result[i]=="/":
                vrem = um_dl(result[i-1],result[i+1],result[i])
                result[i]=str(vrem)
                result.pop(i+1)
                result.pop(i-1)
                i = 0
                print(result)
                print(i)
                break
    while result.count("+") or result.count("-"):
        for y in range(len(result)):
            if result[y]=="+" or result[y]=="-":
                vrem = su_rz(result[y-1],result[y+1],result[y])
                result[y] = str(vrem)
                result.pop(y + 1)
                result.pop(y - 1)
                y = 0
                print(result)
                print(y)
                break
    return result



print(vn(pr))








