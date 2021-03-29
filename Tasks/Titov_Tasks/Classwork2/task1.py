nums = [8, 6, 1, 0, 5, 7, 8, 15, 4]

for i in range(len(nums)):
    minimum = i
    for j in range(i + 1, len(nums)):
        if nums[j] < nums[minimum]:
            minimum = j
    nums[minimum], nums[i] = nums[i], nums[minimum]

print(nums)
