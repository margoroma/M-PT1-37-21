# l = [3, 0, 8, 4, 5]
# for i in range(len(l) - 1):
#         m = i
#         j = i + 1
#         while j < len(l):
#             if l[j] < l[m]:
#                 m = j
#             j = j + 1
#         l[i], l[m] = l[m], l[i]
# print(l)


# import itertools
# for i in itertools.repeat(1):
#     print(i)

# l = [1, 2, 3, 4]
# m = [2, 3, 1, 4]
# if [l[i] == m[i] for i in range(len(l)) if len(l) == len(m)].count(True)==len(l):
#     print('списки равны')
# else:
#     print('списки не равны')

a = 'five thirteen two eleven seventeen two one thirteen ten four eight five nineteen'


d = {
    'five': 5,
    'thirteen': 13,
    'two': 2,
    'eleven': 11,
    'seventeen': 17,
    'one': 1,
    'ten': 10,
    'four': 4,
    'eight': 8,
    'nineteen': 19
}
numbers_list = sorted(list({d[word] for word in a.split()}))
print(numbers_list)
for i, number in enumerate(numbers_list):
    if i == 0:
        continue
    prev_number = numbers_list[i - 1]
    if i % 2 == 0:
        print(number + prev_number)
    else:
        print(number * prev_number)
print(sum(i for i in numbers_list if i % 2 == 1))

