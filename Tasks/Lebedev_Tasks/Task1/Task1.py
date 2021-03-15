sum=20000
month=1
while month<=59:
    sum+=sum*0.0125
    month+=1
print(round(sum, 2))
