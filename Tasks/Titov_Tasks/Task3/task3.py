"""
Работа с файлами

1. Прочитать содержимое файла text.txt
2. Дать пользователю ввести с клавиатуры параметр
"максимальное количество символов в строке", который должен быть больше 15
3. Отформатировать текст с учётом максимального количества символов
4. Записать получившийся текст в новый файл и оповестить об этом пользователя.
"""


def add_spaces(str_, max_len_str, numb_spaces_str):
    numb_replace = max_len_str - len(str_)
    str_add_spaces = str_.replace(numb_spaces_str * ' ', ((numb_spaces_str + 1) * ' '), numb_replace)
    return str_add_spaces


max_len = int(input("Введите ширину строки больше 15: "))

if max_len <= 15:
    print('Ширина страницы должна быть больше 15')
else:
    with open('text.txt', 'r', encoding='utf-8') as f:
        file_text = f.read()
        f.close()

    text_list_1 = []
    for line1 in file_text.split('\n'):
        text1 = ''
        counter = 0
        for word1 in line1.split():
            counter += len(word1)
            if counter >= max_len:
                text1 += '\n'
                counter = len(word1)
            elif text1 != '':
                text1 += ' '
                counter += 1
            text1 += word1
        text_list_1.append(text1)

    column_text = '\n'.join(text_list_1)

    text_list_2 = []
    for line2 in column_text.split('\n'):
        count_space = line2.count(' ')
        if count_space == 0 and len(line2) != max_len:
            line2 += " "
            count_space += 1
        if len(line2) < max_len:
            numb_spaces = round((max_len - len(line2)) // count_space) + 1
            if numb_spaces > 1:
                str_spaces = line2.replace(' ', (numb_spaces * ' '))
                if len(str_spaces) < max_len:
                    str_spaces = add_spaces(str_spaces, max_len, numb_spaces)
            else:
                str_spaces = line2
                if len(str_spaces) < max_len:
                    str_spaces = add_spaces(str_spaces, max_len, numb_spaces)
        else:
            str_spaces = line2
        text_list_2.append(str_spaces)

    final_txt = '\n'.join(text_list_2)

    with open('new_text.txt', 'w', encoding='utf-8') as f:
        f.write(final_txt)
        f.close()
    print('Текст записан в файл new_text.txt')
