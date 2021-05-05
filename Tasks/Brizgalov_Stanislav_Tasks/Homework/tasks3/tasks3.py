q = int(input("Введите количество символов в строке болише 15: "))
if q <= 15:
    print("вы ввели неверное количество символов")
else:
    def func_1(a):
        return len(" ".join(a))


    def func_2(line):
        spaces = q - sum(len(line2) for line2 in line)
        while spaces > 0:
            if len(line) > 1:
                for i in range(len(line) - 1):
                    line[i] += " "
                    spaces -= 1
                    if spaces == 0:
                        break
            else:
                line[0] += " " * (q - len(line[0]))
                break
        final_string = "".join(line)
        return final_string + "\n"


    with open("text.txt", "r", encoding="utf-8") as f:
        text = f.read()
        words = text.split(" ")
        string = []
        text1 = ""
        while words:
            word = words[0]
            words = words[1:]
            if func_1(string + [word]) <= q:
                if "\n" in word:
                    x1, x2 = word.split("\n")
                    word = x1
                    words = [x2] + words
                    text1 += func_2(string + [word, "\n"])
                    string = []
                else:
                    string += [word]
            else:
                text1 += func_2(string)
                string = [word]
        text1 += func_2(string)
    with open("text1.txt", "w", encoding="utf-8") as f:
        f.write(text1)