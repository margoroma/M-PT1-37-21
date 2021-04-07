# 1. Прочитать содержимое файла text.txt

# 2. Дать пользователю ввести с клавиатуры параметр "максимальное количество символов в строке", который должен быть больше 15

# 3. Отформатировать текст с учётом максимального количества символов, при этом если слово целиком не умещается в строке,
# оно должно быть перенесено на следующую, а отступы между словами равномерно увеличены (по аналогии
# с функцией "Выровнять по ширине" текстовых редакторов)

# 4. Записать получившийся текст в новый файл и оповестить об этом пользователя.
# (модуль textwrap использовать нельзя)

import time
import os
os.chdir("C:\\Users\\hp\\GitHub\\M-PT1-37-21\\Tasks\\Lebedev_Tasks\\WH\\Task3H")


max_len = int(input("Введите  количество символов(число должно быть больше 15): "))

while max_len<15:
    print("Вы ввели Число, меньше чем 15!")
    time.sleep(1)
    max_len = int(input("Введите  количество символов(число должно быть больше 15): "))



def number_of_symbols_in_words(a):
    return len(" ".join(a))

def formated_string(words):
    left_wspaces = max_len - sum(len(word) for word in words)
    while left_wspaces > 0:
        if len(words) > 1:
            for i in range(len(words) - 1):
                words[i] += " "
                left_wspaces -= 1
                if left_wspaces == 0:
                    break
        else:
            words[0] += " " * (max_len - len(words[0]))
            break
            
    final_string = "".join(words)
    return final_string + "\n"


with open("text.txt", "r", encoding="utf-8") as f:
    text = f.read()
    words = text.split(" ")
    #print(words)
        
    current_string = []
    text1 = ""

    while words:
        word = words[0]
        words = words[1:]
        if number_of_symbols_in_words(current_string + [word]) <= max_len:
            if "\n" in word:
                x1, x2 = word.split("\n")
                word = x1
                words = [x2] + words

                text1 += formated_string(current_string + [word, "\n"])
                current_string = []
            else:
                current_string += [word]
        else:
            text1 += formated_string(current_string)
            current_string = [word]
        
    text1 += formated_string(current_string)
    print(text1)


with open("text1.txt", "w", encoding="utf-8") as f:
    f.write(text1)


