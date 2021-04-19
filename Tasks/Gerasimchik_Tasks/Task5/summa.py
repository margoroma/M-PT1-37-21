def summa(l):  # Функция суммирования элементов списка любой глубины вложенности
    s = 0  # Накопитель
    for i in l:
        if type(i) == list:  # Если очередной элемент списка является списком, то рекурсивно вызываем сами себя
            s += summa(i)
        else:
            s += i  # Иначе добавляем элемент в накопитель
    return s


def summa1(l):  # То же самое в свернутом виде
    return sum(summa1(i) if isinstance(i, list) else i for i in l)


listing = [[1, 2, [2, 4, [[7, 8], 4, 6]]]]
print(summa(listing))
print(summa1(listing))
