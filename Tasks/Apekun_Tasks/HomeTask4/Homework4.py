

def get_ranges(list):
    list.append(0)
    n = ""
    low = 0
    for i in range (1,len(list)):
        if list[i] != list[i-1]+1:
            if list[low] == list[i-1]:
                n+=str(list[low]) + " "
                low = i
            else:
                n+=str(list[low]) + "-"+str(list[i-1]) + " "
                low = i
    list.pop()
    return n

list = [1,3,5,7,8,9,10,15]
print(get_ranges(list))

def fizzbuzz(number):
    if number % 3 == 0 and number % 5 == 0:
        return "FizzBuzz"
    elif number % 3 == 0:
        return "fizz"
    elif number % 5 == 0:
        return "buzz"
    else:
        return number


for i in range(100):
    print (fizzbuzz(i),end =" ")


