import io


def format_text(page_width):
    with io.open('text.txt', 'r', encoding='utf-8') as text_file:
        raw_text = text_file.read()
        result_text = ''
    for line in raw_text.split('\n'):
        inter_list_1 = []
        inter_list_2 = []
        count = 0
        for word in line.split():
            if count + len(word) <= page_width:
                inter_list_1.append(word)
                count += len(word) + 1
            else:
                inter_list_2.append(inter_list_1)
                inter_list_1 = [word]
                count = len(word) + 1
        inter_list_2.append(inter_list_1)
        for line_str in inter_list_2:
            if len(line_str) == 1:
                result_str = ''.join(line_str) + '\n'
            else:
                a = (page_width - len(''.join(line_str))) // (len(line_str) - 1)
                b = (page_width - len(''.join(line_str))) % (len(line_str) - 1)
                result_str = (a * ' ').join(line_str)
                result_str = result_str.replace((a * ' '), ((a + 1) * ' '), b) + '\n'
            result_text += result_str
        result_text += '\n'
    result_text = result_text[:-2]
    with io.open('formatted_text.txt', 'w', encoding='utf-8') as text_file:
        text_file.write(result_text)
    print('Текст записан в файл formatted_text.txt')


active = True
while active:
    input_page_width = input('Введите ширину страницы\n')
    if input_page_width.isnumeric():
        if int(input_page_width) <= 15:
            print('Ширина страницы должна быть больше 15')
        else:
            format_text(int(input_page_width))
            active = False
    else:
        print('Введите число')
