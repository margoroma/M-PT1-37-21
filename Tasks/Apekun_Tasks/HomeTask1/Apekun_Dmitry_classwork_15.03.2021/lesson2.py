import math

a = int(input("insert a: \n"))
b = int(input("insert b: \n"))
c = int(input("insert c: \n"))

if b < 0 and c < 0:
    print(a,"x^2+",b*(-1), "x+",c*(-1), "= 0")
elif c < 0 and b > 0:
    print(a,"x^2-",b,"x-",c*(-1), "= 0")
elif b < 0 and c > 0 :
    print(a,"x^2+",b*(-1), "x-", c, "= 0")
else:
    print(a,"x^2-",b, "x+", c, "= 0")

D = b*b - 4*a*c
if D > 0:
    print(D)
    x1 = (b - math.sqrt(D))/(2*a)
    x2 = (b + math.sqrt(D))/(2*a)
    print(x1,x2)
else:
    print ( "d < 0")

