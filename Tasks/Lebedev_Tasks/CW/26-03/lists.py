list1 = [1,2,3,4]
list2 = [1,2,3,2]

if len(list1)==len(list2):
    for i in range(len(list1)):
        if list1[i] == list2[i]:
            print('Если станет не идентичным, скажу')
            continue
        else:
            #print('Список не идентичный')
            print("Сказал")
            break
    
