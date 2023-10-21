def isValid(s):
    next_close=[]
    for i in range(len(s)):
        if s[i]=='(':
            next_close.append(')')
        elif s[i]=='{':
            next_close.append('}')
        elif s[i]=='[':
            next_close.append(']')
        else:
            if len(next_close)>0:
                if next_close[len(next_close)-1]==s[i]:
                    del next_close[len(next_close)-1]
                else :
                    return False
            else: 
                return False
            
    if next_close==[]:
        return True
    else:
        return False