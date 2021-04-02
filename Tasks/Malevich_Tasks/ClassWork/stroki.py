spis_one = [8, 10, 1, 2, 5]
spis_two = [4, 3, 5, 7, 18]

if len(spis_one) == len(spis_two):
    spis_one.sort()
    spis_two.sort()
    if spis_one == spis_two:
        print('Списки одинаковые')     
    else: 
        print('Списки разные') 
else:
    print('Длина списков разная')