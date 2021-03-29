stroka = 'five thirteen two eleven seventeen two one thirteen ten four eight five nineteen'
new_list = stroka.split(' ')
print(f'Список из строки - {new_list}')
chisla = [5, 13, 2, 11, 17, 2, 1, 13, 10, 4, 8, 5, 19]
dict_num = {'one': 1,
            'two': 2,
            'four': 4,
            'five': 5,
            'eight': 8,
            'ten': 10,
            'eleven': 11,
            'thirteen': 13,
            'seventeen': 17,
            'nineteen': 19}


for i in new_list:                                          # В числа
    for key in dict_num.keys():
        if i == key:
            new_list[new_list.index(i)] = dict_num.get(key)
print(f'Преобразованный в числа список - {new_list}')


for i in new_list:                                          # Убрать повторы
    if new_list.count(i) > 1:
        new_list.pop(new_list.index(i))
print(f'Список без повторов {new_list}')

new_list.sort()                                    
print(f'Возрастающий список - {new_list}')                  #Сортировка по возрастанию


print(f'Математические операции с элементами списка (построчно - сумма, произведение и т.д.):')
for i in range(len(new_list)-1):                            # Мат. операции
    if i == 0:
        print(new_list[i] + new_list[i+1])
    elif i % 2 != 0:
        print(new_list[i] * new_list[i+1])
    else:
        print(new_list[i] + new_list[i+1])


print(sum(x for x in lis if x%2 != 0))                      # Сумма нечетных чисел в списке
