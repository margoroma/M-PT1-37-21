import math_operations as ops

digits = "0123456789."
fraction = digits
operator = "-+*/^"
parentheses = "()"
spaces = " \n\r\t\v"


#"(24+(8*100))" => ['(','24','+',(,8,*,100,),)] => [tl,tv(24),to(+),tl,tv(8),to(*),tv(100),tr,tr] =>
# => ex([tv(24),to(+),ex([tv(8),to(*),tv(100)])])  => v(824)


def expr_reader(s):
    token_list = []
    accumulator = ''
    for char in s + " ":
        token, accumulator = check_group(char, digits, accumulator)
        if token:
            token_list.extend(token)
        token, accumulator = check_group(char, operator, accumulator, single = True)
        if token:
            token_list.extend(token)
        token, accumulator = check_group(char, parentheses, accumulator, single = True)
        if token:
            token_list.extend(token)
        token, accumulator = check_group(char, spaces, accumulator, accumulate = False)
        if token:
            token_list.extend(token)

    return token_list


def check_group(char, group, accumulator, single = False, accumulate = True): # -> ([token],new_accum)
    accumulate = 1 if accumulate else 0
    if char in group:
        if len(accumulator) == 0 or accumulator[0] in group:
            if single:
                return [char], ""
            else:
                return None, accumulator + char * accumulate
        else:
            if single:
                return [accumulator, char], ""
            else:
                return [accumulator], char * accumulate
    else:
        return None, accumulator


tk_lp = 1
tk_rp = 2
tk_int = 3
tk_op = 4
tk_expr = 5


def make_token(string):
    if string == "(":
        return tk_lp, string
    elif string == ")":
        return  tk_rp, string
    elif string.isdigit():
        return tk_int, string
    elif string in operator:
        return tk_op, string


def tkn_type(tk):
    return tk[0]


def tkn_value(tk):
    return tk[1]


def token_list(string_list):
    return [make_token(token) for token in string_list]

def bracket_check(token_list):
    opened = 0
    for token in token_list:
        if tkn_type(token) == tk_lp:
            opened += 1
        elif tkn_type(token) == tk_rp:
            opened -= 1
        else:
            pass
        if opened < 0:
            return False
    return opened == 0


def nest_expressions(token_list):
    tokens, i = do_nesting(token_list)
    return tokens


def do_nesting(token_list, i = 0):
    tk_list = []
    while i < len(token_list):
        token = token_list[i]
        if tkn_type(token) == tk_lp:
            tokens, i = do_nesting(token_list, i + 1)
            tk_list.append(tokens)
        elif tkn_type(token) == tk_rp:
            break
        else:
            tk_list.append(token)
        i += 1
    return (tk_expr, tk_list), i

def reader(string):
    tokens = expr_reader(string)
    tokens = token_list(tokens)
    if not bracket_check(tokens):
        return "wrong braсket expression"
    tokens = nest_expressions(tokens)

    return tokens

def evaluate(exrpession):
    expr = exrpession[1]
    if len(expr) == 1:
        return evaluate(expr[0])

    op = get_op(expr[1])
    val1 = get_val(expr[0])
    val2 = get_val(expr[2])
    return op(val1, val2)

def get_op(token):
    if tkn_type(token) == tk_op:
        op_name = tkn_value(token)
        return ops.supported_operations[op_name]


def get_val(token):
    t_type = tkn_type(token)
    if t_type == tk_int:
        return float(tkn_value(token))
    elif t_type == tk_expr:
        return evaluate(token)


if __name__ == "__main__":
    while 1:
        string = input("enter expression:")
        if string == "exit":
            break
        print(evaluate(reader(string)))

