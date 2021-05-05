def f(a):
    if not a:
        return a
    if isinstance(a[0], list):
        return f(a[0]) + f(a[1:])
    return a[:1] + f(a[1:])


s = [1, 2, [2, 4, [[7, 8], 4, 6]]]
print(sum(f(s)))
