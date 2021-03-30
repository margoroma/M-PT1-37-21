b = 'five thirteen two eleven seventeen two one thirteen ten four eight five nineteen'
a = {'five': 5, 'thirteen': 13, 'two': 2, 'eleven': 11, 'seventeen': 17, 'two': 2, 'one': 1, 'thirteen': 13,
     'ten': 10, 'four': 4, 'eight': 8, 'five': 5, 'nineteen': 19}

a = set(a.values())
a = sorted(a)
print(a)

k = []
for x in range(len(a) - 1):
    if x == 0:
        k.append(a[x] + a[x + 1])
    elif x % 2 == 1:
        k.append(a[x] * a[x + 1])
    else:
        k.append(a[x] + a[x + 1])
print(k)

z = []
for i in k:
    if i % 2 == 1:
        z.append(i)
print(sum(z))
