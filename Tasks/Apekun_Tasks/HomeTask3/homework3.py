


def length_input():
    length = int(input())

    return length

def text_input():
    with open('text.txt','r') as f:
        words = []
        for line in f:
            words.extend(line.split(" "))

        return words


def divide(words, length):
    lines = []
    current_line = []
    line_length = 0
    for word in words:
        if line_length + len(word)+1 <= length + 1:
            current_line.append(word)
            line_length +=len(word)+1
        else:
            lines.append((current_line,line_length-1))
            current_line = [word]
            line_length = len(word)+1

    return lines


def adjust_line(line, length):
    extra_spaces = length - line[1]
    result_line = line[0][0]
    intervals = len(line[0])-1
    for word in line[0][1:]:
        spaces = int(extra_spaces/intervals)
        result_line += " "*(1+spaces) + word
        intervals -= 1
        extra_spaces -= spaces

    return result_line

def text_format(length):
    text_raw = text_input()
    # print(text)
    text = []
    for words in text_raw:
        for symbol in words:
            if symbol == "\n":
                # print(words)
                words = words[0:-1]
        text.append(words)
    lines = divide(text,length)
    # print(lines)
    formatted = []
    for line in lines:
        formatted.append(adjust_line(line,length))
    for line in formatted:
        # print(line)
        pass
    formatted_text = "\n".join(formatted)
    return  formatted_text

def add_to_file(formatted):
    with open('form_text.txt','w') as formatted_file:
        formatted_file.write(formatted)



def my_formating_programm(length):
    if length < 15:
        print ("your input is less than 15")
        return None
    else:
        divide(text_input(),length)
        text_format(length)
        add_to_file(text_format(length))

        print("file successfulle formatted and copied to file form_text.txt")

my_formating_programm(length_input())
