import random
from random import randint

def forming_list(n):
    s = []
    for x in range(n):
        t = randint(1, 10)
        if t not in s:
            s.append(t)
    return s

def s_sort(list_init): # нет
    for i in range(len(list_init)-1):
        if list_init[i] > list_init[i+1]:
            return False
    return True 

def sort(list_init): # да
    list_sort = sorted(list_init)
    return list_sort

def get_rangers(list_sorted):
    pass

    # for i in len(list_sorted):
    #     if list_sorted[i+1]-list_sorted[i] == 1:


list0 = forming_list(10)
print(f'Список входной: {list0}')     

list1 = s_sort(list0) 
print(list1) 

list1 = sort(list0) 
print(f'Сортированный список: {list1}')