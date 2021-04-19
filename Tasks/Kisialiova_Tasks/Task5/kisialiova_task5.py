l = [1, 2, [2, 4, [[7, 8], 4, 6]]]

rec = lambda x: sum(map(rec, x)) if isinstance(x, list) else x

print(rec(l))
