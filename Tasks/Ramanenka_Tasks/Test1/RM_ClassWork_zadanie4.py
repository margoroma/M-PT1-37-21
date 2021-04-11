stroka = 'five thirteen two eleven seventeen two one thirteen ten four eight five nineteen'
new_list = stroka.split(' ')
print(f'Список из строки - {new_list}')
chisla = [5, 13, 2, 11, 17, 2, 1, 13, 10, 4, 8, 5, 19]


for i in range(len(chisla)):                    # В числа
    new_list[i] = chisla[i]
print(f'Преобразованный в числа список - {new_list}')  


new_list_uniq = []                              # Убрать повторы
for i in new_list:
    if i not in new_list_uniq:
        new_list_uniq.append(i)

print(f'Список без повторов - {new_list_uniq}')     
          

for i in range(len(new_list_uniq)):             # Сортировка по возрастанию
    mini = i
    for j in range(i+1, len(new_list_uniq)):
        if new_list_uniq[j] < new_list_uniq[mini]:
            mini = j
    new_list_uniq[mini], new_list_uniq[i] = new_list_uniq[i], new_list_uniq[mini]

print(f'Возрастающий список - {new_list_uniq}')


print(f'Математические операции с элементами списка (построчно - сумма, произведение и т.д.):')
for i in range(3):                              # Мат. операции
    if i == 0:
        rez = new_list_uniq[i] + new_list_uniq[i+1]
    elif i % 2 != 0:
        rez = new_list_uniq[i] * new_list_uniq[i+1]
    else:
        rez = new_list_uniq[i] + new_list_uniq[i+1]    
    print(rez)


rez = 0
for i in new_list_uniq:                         # Сумма нечетных чисел в списке
    if i % 2 != 0:
        rez += i
print(f'Сумма нечетных чисел в списке равна {rez}')    


