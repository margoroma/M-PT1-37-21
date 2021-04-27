import re
import arith


def calc(string):
    first = re.search(r'-?(\d+(\.\d*)?|\.\d+)', string).group()     # Ищем первое число
    if re.search(r'\d[-+*/]', string):  # Если после него есть мат.символ
        symbol = re.search(r'\d[-+*/]', string).group()[1:]
        symbol_pos = re.search(r'\d[-+*/]', string).end()   # Парсим этот символ
        if symbol == '*' or symbol == '/':  # Смотрим приоритет операции, если высший
            second = re.search(r'(-?\d+(\.\d*)?|\.\d+)', string[symbol_pos:]).group()   # с учетом возможного сочетания мат.операции и отрицательного числа
            string = string.replace(first + symbol + second, simple_math(first, symbol, second))    # И заменяем первое выражение на результат вычислений
            return calc(string)     # Уходим на следующий круг
        else:   # Если приоритет операции низший
            second_end_position = re.search(r'(-?\d+(\.\d*)?|\.\d+)', string[symbol_pos:]).end() + symbol_pos    # Ищем следующий символ мат.операции
            if re.search(r'\d[-+*/]', string[second_end_position - 1:]):   # Если такой символ есть
                next_symbol = re.search(r'\d[-+*/]', string[second_end_position - 1:]).group()[1]
                if next_symbol == '/' or next_symbol == '*':    # Если следующий символ мат.операции имеет высший приоритет
                    second = re.search(r'(-?\d+(\.\d*)?|\.\d+)', string[symbol_pos:]).group()   # то парсим второе число
                    third = re.search(r'(-?\d+(\.\d*)?|\.\d+)', string[second_end_position+1:]).group()     # парсим третье число
                    string = string.replace(second + next_symbol + third, simple_math(second, next_symbol, third))
                    return calc(string)     # Уходим на следующий круг
                else:   # Если следующий символ имеет низший приоритет
                    second = re.search(r'(-?\d+(\.\d*)?|\.\d+)', string[symbol_pos:]).group()   # то выполняем операцию с первыми двумя символами
                    string = string.replace(first + symbol + second, simple_math(first, symbol, second))    #
                    return calc(string)     # Уходим на следующий круг
            else:   # Если такого символа нет
                second = re.search(r'(-?\d+(\.\d*)?|\.\d+)', string[symbol_pos:]).group()   # то выполняем операцию с первыми двумя символами
                string = string.replace(first + symbol + second, simple_math(first, symbol, second))    #
                return string     # Возвращаем итоговую строку

    else:   # Если после числа не нашли мат.операцию
        return string   # Возвращаем итоговую строку


def simple_math(a, b, c):
    if b == '+':
        return str(arith.addition(a, c))
    elif b == '-':
        return str(arith.subtraction(a, c))
    elif b == '*':
        return str(arith.multiplication(a, c))
    else:
        return str(arith.division(a, c))


def curculator(string):
    if re.search(r'\(([^()]+)\)', string):  # Ищем выражение в скобках самой глубокой вложенности
        a = calc(re.search(r'\(([^()]+)\)', string).group(1))   # Отправляем это выражение в обработчик выражений без скобок
        string = string.replace(re.search(r'\(([^()]+)\)', string).group(), a)  # Заменяем выражение в скобках на результат
        return curculator(string)   # Уходим на следующий круг
    elif re.search(r'\d[-+*/]', string):    # Если не нашли в скобках, но нашли сочетание Число+Мат.Символ, значит еще есть выражения без скобок
        return calc(string)     # Отправляем в обработчик выражений без скобок
    else:
        return string   # Иначе у нас больше нет выражений, возвращаем результат


s = '((12.5+(-4-3))*(12+(2-1))+1)+1-1'
print(curculator(s))
