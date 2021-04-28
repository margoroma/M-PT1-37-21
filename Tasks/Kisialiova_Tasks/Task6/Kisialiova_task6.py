import kisialiova_math

OPERATORS = {
    '+': 0,
    '-': 0,
    '*': 1,
    "/": 1
}

OPERATIONS = {
    '+': kisialiova_math.addition,
    '-': kisialiova_math.subtraction,
    '*': kisialiova_math.multiplication,
    '/': kisialiova_math.division
}


def string_to_tokens(input_string):
    output = []
    for char in input_string:
        if char.isdigit():
            if len(output) > 0 and output[-1].isdigit():
                output[-1] += char
            else:
                output.append(char)
        else:
            output.append(char)
    return output


def infix_to_postfix(tokens_list):
    result = []
    operator_stack = []
    for token in tokens_list:
        if token.isdigit():
            result.append(token)
        elif token in OPERATORS:
            while len(operator_stack) > 0 and \
                    operator_stack[-1] in OPERATORS and \
                    OPERATORS[token] <= OPERATORS[operator_stack[-1]]:
                operator_to_move = operator_stack.pop(-1)
                result.append(operator_to_move)
            operator_stack.append(token)
        elif token == '(':
            operator_stack.append(token)
        elif token == ')':
            while len(operator_stack) > 0 and operator_stack[-1] != '(':
                operator_to_move = operator_stack.pop(-1)
                result.append(operator_to_move)
            if operator_stack[-1] == '(':
                operator_stack.pop(-1)
            else:
                raise ValueError('Wrong expression')
    while len(operator_stack) > 0:
        operator_to_move = operator_stack.pop(-1)
        if operator_to_move in ('(', ')'):
            raise ValueError('Wrong expression')
        result.append(operator_to_move)
    return result


def calculate_postfix(tokens_list):
    stack = []
    for token in tokens_list:
        if token.isdigit():
            stack.append(token)
        else:
            operand_b = stack.pop(-1)
            operand_a = stack.pop(-1)
            operation_function = OPERATIONS[token]
            operation_result = operation_function(operand_a, operand_b)
            stack.append(str(operation_result))
    return stack[0]


if __name__ == '__main__':
    expr = input('Введите выражение: ')
    tokens = string_to_tokens(expr)
    postfix = infix_to_postfix(tokens)
    res = calculate_postfix(postfix)
    print(res)
