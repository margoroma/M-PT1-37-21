import re

""" Function for checking data type"""
def is_number(k):
    try:
        float(k)
    except ValueError:
        return False
    return True

"""Function for permorming mathematical operations"""
def operat(stroch):
    stroch = re.findall('[+-/*//()]|-?\d+(?:\.\d+)?', stroch) # splitting of string by characters excluding a point
    if len(stroch) == 2 and stroch[0]=="-":
        stroch = ''.join(stroch) 
        return stroch
    if len(stroch) < 2:
        stroch = ''.join(stroch) 
        return stroch
    else:
        if '/' in stroch:
            ind = stroch.index('/') 
            if stroch[ind+1] != '-':
                if float(stroch[ind+1]) == 0:
                    print('Error: division by zero')
                    return 0
                else:
                    reselt = float(stroch[ind-1]) / float(stroch[ind+1])
            else:
                reselt = float(stroch[ind-1]) / float(stroch[ind+2]) *(-1)
                del stroch[ind+2]
            stroch[ind] = str(reselt)
            del stroch[ind+1]
            del stroch[ind-1]
            stroch = ''.join(stroch)
            return operat(stroch)
        elif '*' in stroch:
            ind = stroch.index('*')
            if stroch[ind+1] != '-': 
                reselt = float(stroch[ind-1]) * float(stroch[ind+1])
            else:
                reselt = float(stroch[ind-1]) * float(stroch[ind+2]) *(-1)
                del stroch[ind+2]
            stroch[ind] = str(reselt)
            del stroch[ind+1]
            del stroch[ind-1]
            stroch = ''.join(stroch)
            return operat(stroch)
        elif '+' in stroch:
            ind = stroch.index('+')
            if stroch[ind+1] != '-': 
                reselt = float(stroch[ind-1]) + float(stroch[ind+1])
            else: 
                reselt = float(stroch[ind-1]) - float(stroch[ind+2])
                del stroch[ind+2]
            stroch[ind] = str(reselt)
            del stroch[ind+1]
            del stroch[ind-1]
            stroch = ''.join(stroch)
            return operat(stroch)
        elif '-' in stroch:
            ind = stroch.index('-')  
            if stroch[ind+1] != '-': 
                reselt = float(stroch[ind-1]) - float(stroch[ind+1])
            else: 
                reselt = float(stroch[ind-1]) + float(stroch[ind+2])
                del stroch[ind+2]
            stroch[ind] = str(reselt)
            del stroch[ind+1]
            del stroch[ind-1]
            stroch = ''.join(stroch)
            return operat(stroch)
        return stroch
"""Function for checking the negative number"""
def check(strok_st):
    if '--' in strok_st:
        strok_st = strok_st.replace('--', '+')
    if '+-' in strok_st:
        strok_st = strok_st.replace('+-', '-')
    return strok_st    

"""The first function to find a nested priority expression"""
def recurs(st):
    st = st.replace(" ","")
    if '(' not in st:
        return st
    else:
        a = st.rfind('(')
        n = len(st[:a])+st[a:].find(')')
        st1 = st[a+1:n]
        res = operat(st1)
        st = st.replace(st[a:n+1],str(res))
        st = check(st)
        return recurs(st)