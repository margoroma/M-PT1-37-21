priority = {"(": 0, ")": 0, "+": 1, "-": 1, "*": 2, "/": 2}

stack_numb = []
stack_oper = []

def calculate(last_oper):
    global stack_numb
    global stack_oper
    x = stack_numb.pop()
    y = stack_numb.pop()
    if last_oper[-1] == "-":
        return stack_numb.append(y - x), stack_oper.pop()
    elif last_oper[-1] == "+":
        return stack_numb.append(y + x), stack_oper.pop()
    elif last_oper[-1] == "*":
        return stack_numb.append(y * x), stack_oper.pop()
    elif last_oper[-1] == "/":
        return stack_numb.append(y / x), stack_oper.pop()


def main(math):
    for idx,el in enumerate(math):
        if el.isdigit():
            if math[idx-1].isdigit() and idx != 0:
                a = str(stack_numb.pop())
                stack_numb.append(int(a+el))
            else:
                stack_numb.append(int(el))
        elif el == "-" and (idx == 0 or math[idx-1] == "("):
            stack_numb.append(-1)
            stack_oper.append("*") 
        elif el == "(":
            stack_oper.append(el)
        elif el == ")":
            while priority.get(stack_oper[-1]) != 0:
                calculate(stack_oper[-1])
            else: 
                if el == ")" and stack_oper[-1] == "(":
                    stack_oper.pop()
        elif stack_oper == []:
            stack_oper.append(el)
        elif stack_oper:
            while stack_oper and priority.get(el) <= priority.get(stack_oper[-1]) and len(stack_numb) >= 2:
                calculate(stack_oper[-1])
            stack_oper.append(el)
    while stack_oper:
        calculate(stack_oper[-1])
    return stack_numb[0]