def sorting_numbers(nums):
    for i in range(len(nums)):
        lowest_value = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[lowest_value]:
                lowest_value = j
        nums[i], nums[lowest_value] = nums[lowest_value], nums[i]


random_numbers = [25, 21, 3, 55, 6, 16]
sorting_numbers(random_numbers)
print(random_numbers)


l = [1]
for x in l:
    l.append(x + 1)
    print(x)

a = [1, 2, 3, 5]
b = [1, 3, 2, 7]

if len(a) == len(b):
    for i in range(len(a)):
        if a[i] == b[i]:
            print('Equal')
        else:
            print('Not equal')

string = {'five': 5, 'thirteen': 13, 'two': 2, 'eleven': 11, 'seventeen': 17,
          'two': 2, 'one': 1, 'thirteen': 13, 'ten': 10, 'four': 4, 'eight': 8,
          'five': 5, 'nineteen': 19}

values = string.values()
no_dublicates = set(values)
no_dublicates2 = list(no_dublicates)
list_mult = [((x * y), (x + y)) for (x, y) in zip(no_dublicates2[:-1], no_dublicates2[1:])]

unzipped_object = zip(*list_mult)
unzipped_list = list(unzipped_object)
unzipped_list = [y for x in unzipped_list for y in x]
print(unzipped_list)
sum_odds = sum(n for n in unzipped_list if n % 2)
print(sum_odds)
