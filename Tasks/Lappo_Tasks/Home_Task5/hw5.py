x=[1, 2, [2, 4, [[7, 8], 4, 6]]]


def sumlists(numList):
    rezult=0
    for i in numList:
        if type(i) == int:
            rezult += i
        else:
            rezult += sumlists(i)
    return rezult

print(sumlists(x))