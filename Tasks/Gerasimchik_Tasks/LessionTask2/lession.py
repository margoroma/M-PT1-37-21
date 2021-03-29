# генератор списков
a = 'five thirteen two eleven seventeen two one thirteen ten four eight five nineteen'

digit_lexicon = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
    'ten': 10,
    'eleven': 11,
    'twelve': 12,
    'thirteen': 13,
    'fourteen': 14,
    'fifteen': 15,
    'sixteen': 16,
    'seventeen': 17,
    'eighteen': 18,
    'nineteen': 19,
    'twenty': 20,
}
a = list(set([digit_lexicon[i] for i in a.split(' ')]))
print(a)
y = 0
for i in range(len(a)):
    if i % 2 != 0:
        print(a[i-1]*a[i])
        if i+1 < len(a):
            print(a[i]+a[i+1])
    if a[i] % 2 != 0:
        y += a[i]
print(f'сумма нечетных чисел {y}')
