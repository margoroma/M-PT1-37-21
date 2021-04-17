def fizz_buzz(n):
    if n % 3 == 0 and n % 5 == 0:
        print('fizzbuzz')
    elif n % 3 == 0:
        print('fizz')
    elif n % 5 == 0:
        print('buzz')
    else:
        print('not divisible')

n = int(input('enter number:'))
fizz_buzz(n)
