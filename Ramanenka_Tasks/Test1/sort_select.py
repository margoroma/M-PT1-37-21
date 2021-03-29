from random import randint

n = 10
s = []

for m in range(n):
    s.append(randint(1, 99))
print(f'Массив из чисел: {s}')

def sor(arr):
    for i in range(len(s)):
        min = i
        for k in range(i+1, len(s)):
            if s[k] < s[min]:
                min = k
        s[i], s[min] = s[min], s[i]
    print(f'Отсортированный массив: {arr}')

sor(s)