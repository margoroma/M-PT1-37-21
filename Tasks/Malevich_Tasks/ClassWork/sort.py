sort_numb = input('Введите числа через пробел: ')
sort_numb = sort_numb.replace(' ', ',')
sort_numb = sort_numb.split(',')
print(sort_numb)

for i in range(len(sort_numb) - 1):
    min = i
    for j in range(i + 1, len(sort_numb)):
        min = j
        if int(sort_numb[j]) < int(sort_numb[i]):
            sort_numb[min], sort_numb[i] = sort_numb[i], sort_numb[min]

print(sort_numb)
