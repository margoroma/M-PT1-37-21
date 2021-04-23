l=['1','11','12','22','2','13','30','33']



rez=sorted(list(map(int, list(filter(lambda l: int(l)*int(l) % 2 != 0, l)))))


print(rez)