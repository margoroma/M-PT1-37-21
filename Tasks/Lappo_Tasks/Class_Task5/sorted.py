import random
x = [3,1,2,8]

def is_sorted(x_sort):
    if sorted(x_sort)==x:
        rez="Отсортировано!"
    else:
        rez="Не отсортировано!"
    return rez

def get_random(x_random):
    while True:
        x_rez = random.randint(0,len(x_random)-1) 
        y_rez = random.randint(0,len(x_random)-1) 
        z_rez=x_rez==y_rez

        if z_rez==False:
            return x_rez, y_rez

def swap(x_swap, y_swap, z_swap):
        x_swap[y_swap], x_swap[z_swap] = x_swap[ z_swap], x_swap[y_swap]
        rezswap=x_swap
        return rezswap




rezpr="Отсортировано!"
iter=0

print(x)

while is_sorted(x)!=rezpr:
    get = get_random(x)
    x=swap(x, get[0], get[1])
    iter +=1
else:
    print(iter)
    print(x)
