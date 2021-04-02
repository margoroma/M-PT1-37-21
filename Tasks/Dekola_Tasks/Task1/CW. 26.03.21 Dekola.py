d = {'five': 5, 'thirteen': 13, 'two': 2, 'eleven': 11, 'seventeen': 17, 'two': 2, 'one': 1, 'thirteen': 13, 
'ten': 10, 'four': 4, 'eight': 8, 'five': 5, 'nineteen': 19} #сделать словарь и ключи к нему

val = d.values() #превратить словарь в список

dub1 = list(set(val)) #превратить во множество, читаемое как отсортированный список

print(dub1, 'Список')


for y in range(len(dub1)): #открываем цикл на длину списка
    if y == len(dub1) - 1: #указываем, чтобы кампуктер не выходил за последнюю позицию, т.е. доходит до позиции 9, и все
        break 
    if (y + 1) % 2 != 0:  #по позиции нечет
        print(dub1[y] * dub1[y + 1]) #в квадратных скобках позиция
    if (y + 1) % 2 == 0:  #по позиции чет
        print(dub1[y] + dub1[y + 1])

res = 0
for i in range(len(dub1)):
    if dub1[i] % 2 != 0:
        res = res + dub1[i]
print(res)

