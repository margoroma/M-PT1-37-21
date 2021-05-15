# Реализовать класс, который в зависимости от некоторых параметров (например, количество комнат),
# будет "строить" лабиринт.
# *Визуализировать построенный лабиринт.
from random import randint
class labirint(object):
    def sozdanie(kol):
        labirint_start = {}
        def chern_lab(labirint_1):
            def dveri(komnaty, i):
                naz_k = "k" + str(i + 1)  # комната i для которой строим двери
                quantity_doors = randint(1, 2)  # количество дверей в каждой комнате от 1 до 4
                dveri = []
                postroeno_dverei = 0
                while quantity_doors != postroeno_dverei:
                    dver_in = randint(1, kol)
                    if dver_in == i + 1:
                        continue
                    dver_in = "k" + str(dver_in)
                    if dveri.count(dver_in):
                        continue
                    dveri.append(dver_in)
                    postroeno_dverei = postroeno_dverei + 1
                komnaty[naz_k] = dveri
                return komnaty

            for i in range(kol):
                labirint_1 = dveri(labirint_1, i)

            return labirint_1
        def dveri_sviaz_proverka(komnaty):
            for key in komnaty:
                door_not_update = komnaty[key]  # комната не проверенная
                for i in range(len(door_not_update)):  # для каждой двери не проверенно комнаты который называет perehod
                    perehod = komnaty[door_not_update[i]]

                    if perehod.count(key):
                        continue
                    else:
                        if len(perehod) >= kol - 1:
                            perehod.pop()
                            perehod.append(key)

                            dveri_sviaz_proverka(komnaty)
                        else:

                            komnaty[door_not_update[i]].append(key)
                            continue
            return komnaty
        labirint = chern_lab(labirint_start)
        itog_lab = dveri_sviaz_proverka(labirint)
        return(itog_lab)

p = labirint.sozdanie(10)


print(p)

