a = 'five thirteen two eleven seventeen two one thirteen ten four eight five nineteen'

digit_lexicon = (
    'zero',
    'one',
    'two',
    'three',
    'four',
    'five',
    'six',
    'seven',
    'eight',
    'nine',
    'ten',
    'eleven',
    'twelve',
    'thirteen',
    'fourteen',
    'fifteen',
    'sixteen',
    'seventeen',
    'eighteen',
    'nineteen',
    'twenty',
)
a = a.split(' ')
a = list(set([digit_lexicon.index(i) for i in a]))
a.sort()
a.append(0)
for i in a:
    if i == a[-1]:
        break
    if a.index(i) % 2 != 0:
        print('умножение', a[a.index(i) - 1] * i)
        if a.index(i) + 1 < len(a) - 1:
            print('сумма', i + a[a.index(i) + 1])
    if i % 2 != 0:
        a[-1] -= i
print(f'сумма нечетных чисел {-a[-1]}')
