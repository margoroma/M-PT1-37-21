def fizzbuzz(l):
    for i in l:
        if not i % 3:
            if not i % 5:
                print('FizzBuzz')
            else:
                print('Fizz')
        elif not i % 5:
            print('Buzz')
        else:
            print(i)


def fizzbuzz_2(l):
    for i in l:
        if not i % 15:
            print('FizzBuzz')
        elif not i % 5:
            print('Buzz')
        elif not i % 3:
            print('Fizz')
        else:
            print(i)


listing = [x for x in range(1, 100)]
fizzbuzz(listing)
fizzbuzz_2(listing)

# утянуто с хабра, но вариант понравился, сам бы не додумался
[print(['Fizz', '', ''][i % 3] + ['Buzz', '', '', '', ''][i % 5] or i) for i in range(1, 100)]
