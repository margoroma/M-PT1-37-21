

def list_sum(somelist):
    summ = 0
    for numb in somelist:
        if type(numb) != list:
            summ+=numb
        else:
            summ+= list_sum(numb)
    return summ

l = [1,2,[2,4,[[7,8],4,6]]]

print(list_sum(l))