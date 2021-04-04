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

string = 'five thirteen two eleven seventeen two one thirteen ten four eight five nineteen'.split(' ')
dict_for_string = {'five': 5, 'thirteen': 13, 'two': 2, 'eleven': 11, 'seventeen': 17,
                   'one': 1, 'ten': 10, 'four': 4, 'eight': 8, 'nineteen': 19}
str_to_num = set()
for s in string:
    str_to_num.add(dict_for_string[s])

no_duplicates = list(str_to_num)
print(no_duplicates)

summery = []
last_action = True

for i in range(len(no_duplicates)):
    if i % 2 != 0:
        if last_action:
            summery.append(no_duplicates[i] + no_duplicates[i - 1])
            last_action = False
        else:
            summery.append(no_duplicates[i] * no_duplicates[i - 1])
            last_action = True
print(summery)
sum_odds = sum(n for n in summery if n % 2)
print(sum_odds)
