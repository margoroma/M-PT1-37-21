stroka = 'five thirteen two eleven seventeen two one thirteen ten four eight five nineteen'
new_list = stroka.split(' ')
print(f'Список из строки - {new_list}')
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
    new_list[new_list.index(i)] = dict_num.get(i)
print(f'Преобразованный в числа список - {new_list}')

new_list = list(sorted(set(new_list)))
print(f'Упорядоченный список без повторов {new_list}')      # Без повторов + сортировка

print(f'\nМатематические операции с элементами списка:')
for i in range(len(new_list)-1):                            # Мат. операции
    if i == 0:
        print(f'Сумма первых 2-х элементов равна {new_list[i] + new_list[i+1]}')
    elif i % 2 != 0:
        print(f'Произведение {i+1}-го и {i+2}-го элементов равно {new_list[i] * new_list[i+1]}')
    else:
        print(f'Сумма {i+1}-го и {i+2}-го элементов равна {new_list[i] + new_list[i + 1]}')

print(f'\nСумма нечетных чисел в списке равна {sum(i for i in new_list if i%2 != 0)}')  # Сумма нечетных чисел в списке