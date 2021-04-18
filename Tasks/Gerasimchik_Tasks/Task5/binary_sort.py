def binary(listing, n, min_value, max_value):
    if listing[len(l)-1] < n or listing[0] > n:
        return -1
    mid = min_value + (max_value - min_value) // 2
    if listing[mid] < n:
        return binary(listing, n, mid + 1, max_value)
    elif listing[mid] > n:
        return binary(listing, n, min_value, mid - 1)
    else:
        return mid


l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
print(binary(l, 4, 0, len(l)))
