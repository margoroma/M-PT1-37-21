arr = [8,4,6,2,1,3,5,7]
for i in range(len(arr)):
    for j in range(len(arr)):
        if arr[i] < arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
        j+=1
print(arr)