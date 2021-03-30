с = "five thirteen two eleven seventeen two one thirteen ten four eight five nineteen"
c = с.split(" ")
for i in range(len(c)):
    c[i] = {"five": 5, "thirteen": 13, "two": 2, "eleven": 11, 'seventeen': 17, 'one': 1,
            "ten": 10, "four": 4, "eight": 8, "nineteen": 19}[c[i]]
print(c)
c = list(set(c))
print("Отсортированный список и без дублей:", c)
for y in range(len(c)):
    if y == int(len(c) - 1): break
    if c[y] % 2 != 0: print(y, "действие =", c[y] + c[y + 1])
    if c[y] % 2 == 0: print(y, "действие =", c[y] * c[y + 1])
c = [c[z] for z in range(len(c)) if c[z] % 2]
print("Все нечетные:", c)
print(sum(c))
