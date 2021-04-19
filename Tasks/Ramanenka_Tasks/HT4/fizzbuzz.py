""" Больше всего понравилось это:
"""
for i in range(1,101):
    print('Fizz'*(i%3<1) + (i%5<1)*'Buzz' or i)

""" Такое же, только в список оформлено:
"""
print(list("Fizz"*(i%3<1)+"Buzz"*(i%5<1) or i for i in range(1,101)))