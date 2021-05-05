text = list()
with open('text.txt', 'r+') as t:
    text = [l.strip() for l in t.read().split()]
    text = ' '.join(text)
prompt = int(input('введите колличество символов в одной троке,также количесто должно быть больше 15 '
                   'символов: '))
if prompt > 15:
    new_text = ''
    word = ''
    line = ''
    string_length = prompt
    for letter in text:
        word += letter
        if letter == ' ' or letter == ',' or letter == '.':
            line += word
            word = ''
        if len(line) + len(word) >= string_length:
            line_without_spaces = line.strip()
            free_spaces = string_length - len(line_without_spaces)
            all_spaces_in_line = line_without_spaces.count(' ')
            if all_spaces_in_line == 0:
                all_spaces_in_line += 1
            additional_spaces = free_spaces // all_spaces_in_line
            some_spaces = free_spaces % all_spaces_in_line
            updated_line = line_without_spaces.replace(' ', ' ' + (' ' * additional_spaces))
            if some_spaces != 0:
                space_index = updated_line.find(' ')
                updated_line_in_array = list(updated_line)
                updated_line_in_array[space_index] = '  ' * some_spaces
                updated_line = ''.join(updated_line_in_array)
            new_text += updated_line + '\n'
            # print(updated_line)
            line = ''
            additional_spaces = 0
            all_spaces_in_line = 0

    with open('updated_text.txt', 'w') as updated_file:
        updated_file.write(new_text)
        print('Новый файл находиться в updated_text.txt')
else:
    print('Число должно быть больше 15,попробуйте перезапустить программу')