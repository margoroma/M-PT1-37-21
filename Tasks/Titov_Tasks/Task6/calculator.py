from decimal import Decimal

opers = {'+': (1, lambda x, y: x + y),
         '-': (1, lambda x, y: x - y),
         '*': (2, lambda x, y: x * y),
         '/': (2, lambda x, y: x / y)
         }
simb = ["(", ")"]


def convert_to_list(user_input):
    numb = ''
    lst_input = []
    for pos, char in enumerate(user_input):
        if char in '1234567890.':
            numb += char
        elif numb:
            if pos > 0:                             # for equations such a*(-b)
                if user_input[pos - 2] == "-" and user_input[pos - 3] == "(":
                    lst_input = lst_input[:-1]
                    lst_input.append(Decimal(numb) * (-1))
                    numb = ''
                else:
                    lst_input.append(Decimal(numb))
                    numb = ''
        if char in opers or char in simb:
            if char == "-" and pos == 0:              # for equations such -a*b
                change_simb = [-1, "*"]
                lst_input += change_simb
            else:
                lst_input.append(char)
    if numb:
        lst_input.append(Decimal(numb))
    return lst_input


def stack(user_input_list):
    stack_oper = []
    for elem in user_input_list:
        if elem in opers:
            while len(stack_oper) > 0 and stack_oper[-1] != '(' \
                    and opers[elem][0] <= opers[stack_oper[-1]][0]:
                yield stack_oper.pop()
            stack_oper.append(elem)
        elif elem == ')':
            while len(stack_oper) > 0:
                last_oper = stack_oper.pop()
                if last_oper == '(':
                    break
                yield last_oper
        elif elem == '(':
            stack_oper.append(elem)
        else:
            yield elem
    while len(stack_oper) > 0:
        yield stack_oper.pop()


def calc(stack_list):
    stack_numb = []
    for stack_elem in stack_list:
        if stack_elem in opers:
            second_numb = stack_numb.pop()
            if stack_elem == "/" and second_numb == 0:
                return "ОШИБКА. Деление на ноль"
                break
            first_numb = stack_numb.pop()
            stack_numb.append(opers[stack_elem][1](first_numb, second_numb))
        else:
            stack_numb.append(stack_elem)
    return stack_numb[0]
