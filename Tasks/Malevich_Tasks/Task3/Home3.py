numb_sym = int(input("Введите количество символов больше 15: \n"))
if numb_sym < 15:
    print("Вы ввели неверное количество")
else:
    with open("text.txt", "r", encoding="utf-8") as f:
        text_f = f.read()
        f.close()

indent = []
lines = text_f.splitlines()
for i in lines:                               
    indent.append(i)

for index, elem in enumerate(indent):
    lower_index = 0
    upper_index = 0
    new_text = []
    last_position = elem.rindex(' ')
    while upper_index < len(elem):
        upper_index = elem.rindex(' ', lower_index, lower_index + numb_sym)
        if upper_index == last_position:
            upper_index = len(elem)
        #if upper_index - lower_index > numb_sym:
            #print('error!')
        index = elem[lower_index:upper_index].strip()
        lower_index = upper_index
        if len(index) <= numb_sym:
            words = index.split() 
            num_words = numb_sym - (len(''.join(words)) + (len(words)-1))
            while num_words != 0 and len(words) > 1:
                for i in range(len(words)-1):
                    if num_words != 0:
                        words[i] = words[i] + ' '
                        num_words -= 1
                    else:
                        break 
            index = ' '.join(words)
            new_text.append(index)
        else:
            new_text.append(index)
    print_text ='\n'.join(new_text)
    #print(print_text)
    with open("text_new.txt", "a", encoding="utf-8") as f:
        f.write(print_text + "\n")
print("Текст записан в новый файл: text_new.txt")   