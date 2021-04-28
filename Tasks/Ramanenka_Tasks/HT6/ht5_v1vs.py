import re

# st = input('equation: \n')
st = '(25 *(5+ (1-3/10*4)/2))'
st = st.replace(" ","")

def is_number(k):
    try:
        float(k)
    except ValueError:
        return False
    return True

def ret(s):
    s = re.findall('[+-/*//()]|-?\d+(?:\.\d+)?', s)
    if len(s) == 2 and s[0]=="-":
        s = ''.join(s) 
        return s
    
    if len(s) < 2:
        s = ''.join(s) 
        return s
        
    
    else:
        if '/' in s:
            ind = s.index('/')  
            reselt = float(s[ind-1]) / float(s[ind+1])
            s[ind] = str(reselt)
            del s[ind+1]
            del s[ind-1]
            s = ''.join(s)
            return ret(s)
        elif '*' in s:
            ind = s.index('*')  
            reselt = float(s[ind-1]) * float(s[ind+1])
            s[ind] = str(reselt)
            del s[ind+1]
            del s[ind-1]
            s = ''.join(s)
            return ret(s)
        elif '+' in s:
            ind = s.index('+')  
            reselt = float(s[ind-1]) + float(s[ind+1])
            s[ind] = str(reselt)
            del s[ind+1]
            del s[ind-1]
            s = ''.join(s)
            return ret(s)
        elif '-' in s:
            ind = s.index('-')  
            reselt = float(s[ind-1]) - float(s[ind+1])
            s[ind] = str(reselt)
            del s[ind+1]
            del s[ind-1]
            s = ''.join(s)
            return ret(s)
        return s
def check(stroka_st):
    pass #+-  /-  *- --
def rec(st):
    if '(' not in st:
        return st
    else:
        a = st.rfind('(')
        n = st.find(')')
        st1 = st[a+1:n]
        res = ret(st1)
        st = st.replace(st[a:n+1],str(res))
        #check(st)
        #leer aplicar def
        
        return rec(st)

print(rec(st))


