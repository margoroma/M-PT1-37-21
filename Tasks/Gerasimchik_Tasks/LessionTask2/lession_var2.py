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
for i in range(len(a)-1):
    if i % 2 != 0:
        print(a[i - 1] * a[i])
        if i + 1 < len(a) - 1:
            print(a[i] + a[i + 1])
    if a[i] % 2 != 0:
        a[-1] += a[i]
print(f'сумма нечетных чисел {a[-1]}')
