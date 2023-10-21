def myAtoi(s):
    if len(s)==0:
        return 0
    sign='positive'
    sign_found=False
    isfloat=False
    for i in range(len(s)):
        if s[i]=='.':
            isfloat=True
    if isfloat==True:
        s=float(s)
        s=int(s)
        s=str(s)
        
    i=0
    while not s[i].isdigit():
        if sign_found==True:
            return 0
        if s[i]=='-' and sign_found==False:
            sign='negative'
            sign_found=True     
            s=s.replace(s[i],"",1)    
        elif s[i]=='+' and sign_found==False:       
            sign='positive'
            sign_found=True  
            s=s.replace(s[i],"",1) 
        elif s[i]==' ':
            s=s.replace(s[i],"",1)
        else:
            return 0    
        if len(s)==0:
            return 0
    
    """ i=len(s)-1  
    while not s[i].isdigit():
        i-=1 """
    
    string=''
    i=0
    while i<len(s):
        if s[i].isdigit():
            string+=s[i]
            i+=1
        else:
            break
    
    """for z in range(i+1):
        string+=s[z] """
    number=int(string)
    if sign=='negative':
        number*=-1
    if number<-2**31:
        number=-2**31
    elif number>2**31 - 1:
        number=2**31-1
    return number