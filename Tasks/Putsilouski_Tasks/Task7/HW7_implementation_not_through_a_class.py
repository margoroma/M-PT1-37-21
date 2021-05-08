# Реализовать классы для имитации структуры лабиринта, включающие следующие объекты:
# -стена;
# -дверь;
# -комната;
# Реализовать класс, который в зависимости от некоторых параметров (например, количество комнат), будет "строить" лабиринт.
# *Визуализировать построенный лабиринт.

from random import random, randrange, randint

kol = int(input("Количетсво комнат:\n"))
komnaty = {}




def dveri(komnaty, kol, i):
    naz_k = "k" + str(i + 1) # комната i для которой строим двери
    quantity_doors = randint(1,4) # количество дверей в каждой комнате от 1 до 4
    dveri = []
    postroeno_dverei = 0
    while quantity_doors != postroeno_dverei:
        dver_in = randint(1, kol)
        if dver_in == i+1:
            continue
        dver_in = "k" + str(dver_in)
        if dveri.count(dver_in):
            continue
        dveri.append(dver_in)
        postroeno_dverei=postroeno_dverei+1
    komnaty[naz_k] = dveri

    return komnaty




for i in range(kol):
    komnaty = dveri(komnaty, kol, i)
    print(komnaty)

