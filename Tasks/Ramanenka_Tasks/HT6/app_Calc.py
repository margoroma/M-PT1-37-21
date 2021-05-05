from ht6_calculator_with_brackets import recurs


"""Enter the expression or continue with default expression"""
expression = '(25 -(5- (1-2))/(5-8))'
# equation = input('Expression is: \n')
results = float(recurs(expression))
print(f'Result is: {results}')