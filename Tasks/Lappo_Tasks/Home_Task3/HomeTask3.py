import os
import codecs

def user_length():
    x=0
    while x<15:
        x=int(input("Введите максимальное количество символов в строке, больше 15 :"))
        if x<15:
            print("БОЛЬШЕ 15 а не меньше!")
    else:
        print("Спасибо")

        return x

def src_text():
    os.chdir("d:\\PYTHON-IT-AK\\GitHub\\M-PT1-37-21\\Tasks\\!Tasks\\HomeWork3\\")
    with codecs.open("text.txt", "r", "utf_8_sig") as f:
        lines=[]
        rez=[]
        lines = f.readlines()
        f.close()
        for line in lines:
            strr = line.split() 
            rez.extend(strr)
        return rez


def dividing(words, length):
    lines = []
    current_line = []
    line_length = 0
    for word in words:
        if line_length + len(word)+1 <= length+1:
            current_line.append(word)
            line_length +=len(word)+1
        else:
            lines.append((current_line,line_length-1))
            current_line = [word]
            line_length = len(word)+1
    lines.append((current_line,line_length-1))
    return lines


def add_line(line, length):
    extra_spaces = length - line[1]
    result_line = line[0][0]
    intervals = len(line[0])-1
    for word in line[0][1:]:
        if extra_spaces==0:
            result_line +=  " "+word
        else:
            spaces = int(extra_spaces/intervals)
            result_line += " "*(1+spaces) + word
            intervals -= 1
            extra_spaces -= spaces
    return result_line

def formating(length):
    text_raw = src_text()
    text = []
    for words in text_raw:
        for symbol in words:
            if symbol == "\n":
                words = words[0:-1]
        text.append(words)
    lines = dividing(text,length)
    formatted = []
    for line in lines:
        formatted.append(add_line(line,length))
    for line in formatted:
        pass
    formatted_text = "\n".join(formatted)
    return  formatted_text

def add_to_file(formatted):
    os.chdir("d:\\PYTHON-IT-AK\\GitHub\\M-PT1-37-21\\Tasks\\Lappo_Tasks\\Home_Task3\\")
    with codecs.open("newtext.txt", "w", "utf_8_sig") as f:
        f.write(formatted)





x=user_length()
y=dividing(src_text(),x)
z=formating(x)
zz=add_to_file(formating(x))

print("Файл создан: "+os.getcwd()+"\\newtext.txt")