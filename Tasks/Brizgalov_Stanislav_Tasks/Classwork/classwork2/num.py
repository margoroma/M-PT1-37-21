b = 'five thirteen two eleven seventeen two one thirteen ten four eight five nineteen'
a = {'five': 5, 'thirteen': 13, 'two': 2, 'eleven': 11, 'seventeen': 17, 'two': 2, 'one': 1, 'thirteen': 13,
     'ten': 10, 'four': 4, 'eight': 8, 'five': 5, 'nineteen': 19}

a = set(a.values())
a = list(a)
a = sorted(a)
print(a)

a = [a[0] + a[1], a[1] * a[2], a[2] + a[3], a[3] * a[4], a[4] + a[5], a[5] * a[6], a[6] + a[7], a[7] * a[8],
     a[8] + a[9]]
print(a)

z = []
for i in a:
    if i % 2 == 1:
        z.append(i)
print(sum(z))
