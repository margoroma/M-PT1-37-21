max_length = int(input("Введите максимальное кол-во символов, начиная с 15:\n"))

def current_symbols_in_words(a):
    return len(" ".join(a))

def format_string(words):
    left_whitespaces = max_length - sum(len(word) for word in words)
    while left_whitespaces > 0:
        if len(words) > 1:
            for i in range(len(words) - 1):
                words[i] += " "
                left_whitespaces -= 1
                if left_whitespaces == 0:
                    break
        else:
            words[0] += " " * (max_length - len(words[0]))
            break
            
    final_string = "".join(words)
    return final_string + "\n"

if max_length < 15:
    print("Вы ввели недостаточное кол-во символов")
else:
    with open("text.txt", "r", encoding="utf-8") as t:
        text = t.read()
        words = text.split(" ")
            
        current_string = []
        new_text = ""

        while words:
            word = words[0]
            words = words[1:]
            if current_symbols_in_words(current_string + [word]) <= max_length:
                if "\n" in word:
                    a, b = word.split("\n")
                    word = a
                    words = [b] + words

                    new_text += format_string(current_string + [word, "\n"])
                    current_string = []
                else:
                    current_string += [word]
            else:
                new_text += format_string(current_string)
                current_string = [word]
            
        new_text += format_string(current_string)
    print("Отформатированный текст находится в файле: new_text.txt")


    with open("new_text.txt", "w", encoding="utf-8") as writer:
        writer.write(new_text)