def sum_all(L):
    sum = 0 
    for i in L:
        if isinstance(i, list):
            sum += sum_all(i)
        else:
            sum += i
    return sum

L = [1, 2, [2, 4, [[7, 8], 4, 6]]]
print(f"Сумма: {sum_all(L)}")