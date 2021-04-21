import sys

num_of_symbols = int(input('Введите число больше 15: '))
if num_of_symbols <= 15:
    sys.exit("Число должно быть больше 15. Перезапустите программу, если хотите продолжить.")   

with open("text.txt", "r", encoding="utf-8") as f:
    text_init = f.read()

def div_text(text_):
    """ разбиение полного текста по абзацам (строки в изначальном тексте)
        на выходе - список строк (абзацев) текста
    """
    result = []
    lines = text_.splitlines()                                   # деление текста по абзацам
    for i in lines:                                              # каждый абзац в строку списка
        result.append(i)
    return result    

def form_text(list_text, num):
    """ разбиение абзацев на строки в зависимости от длины строки без переносов слов;
        на выходе - список строк для одного абзаца
    """
    list_lines = []                                             # создание нового списка из строк для абзаца
    while len(list_text) > 0:
        line = list_text[:num]
        if len(list_text) <= num:                               # короткий абзац без изменений
            line = list_text
            last_text = list_text[len(line):]
            list_text = last_text
        elif line[-1] != ' ' and list_text[num:num+1] != ' ':       # проверка на резку слова в конце строки      
            ind_last_space = line.rfind(' ')                        # ищется последний пробел в line
            line = list_text[:ind_last_space]                       # по последнему пробелу формаруется строка
            last_text = list_text[len(line)+1:]                     # оставшийся текст после выделения строки
            list_text = last_text    
        else:
            last_text = list_text[len(line):]
            list_text = last_text
        
        list_lines.append(line)
    return list_lines                                             # для 1 абзаца   

def strech_text(spisok_lines, num):
    """ 'растягивание' по ширине строк в зависимости от длины строки;
        на выходе - список готовых строк для одного абзаца
    """
    list_new = []   
    for item in spisok_lines: 
        if len(item) == num: 
            if item[0] == ' ':              # проверка на пробел в начале строки нужной длины 
                item.replace(' ', '')
            elif item[-1] == ' ':           # проверка на пробел в конце строки нужной длины
                item.replace(' ', '')    
            else:
                list_new.append(item)
                continue
        if item == spisok_lines[-1] and len(spisok_lines) != 1: # REVIS    # последняя строка абзаца без изменений
            list_new.append(item)
            continue
        if len(item) <= num and len(spisok_lines) != 1:                # сравнение с заданной длиной строки
            line = item                                    
            words = item.split()            # деление строки на слова (для удаления лишних пробелов, если таковые имеются)
            num_spaces = num - (len(''.join(words)) + (len(words)-1)) # количество недостающих пробелов
            while num_spaces != 0 and len(words) > 1:
                for i in range(len(words)-1): # количество слов, после которых добаляются пробелы (последнее слово исключается)
                    if num_spaces != 0 :
                        if len(line) <= num: # добавление пробелов после каждого слова, кроме последнего
                            words[i] = words[i] + ' '
                            num_spaces -= 1
                    else:
                        break
            line = ' '.join(words)
            list_new.append(line)
        elif len(spisok_lines) == 1 and len(item) < 16:  # если в абзаце одно короткое предложение (<16 символов), то оно не обрабатывается
            line = item 
            list_new.append(line)
    return list_new


list_absaz = div_text(text_init)   # обращение к функции для создания списка из строк-абзацев

list2 = []
for i in list_absaz: 
    list2.append(form_text(i, num_of_symbols)) # обращение к функции для создания строк; на выходе список из списков

list3 = []
for i in list2:
    list3.append(strech_text(i, num_of_symbols)) # обращение к функции для форматирования строк по ширине; на выходе список из списков с добавленными пробелами между словами в строках

with open("text1.txt", "w", encoding="utf-8") as f:
       
    for st in list3:
        for j in st:
            f.write(j + '\n')
          
print(f'Текст записан в файл "text1.txt" в текущей директории')
