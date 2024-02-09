import re

def calculations(mylist):  # function that makes simple computations with +,-,* (without parentheses)
    i=0    
    while i<len(mylist):
        if mylist[i]=='*':
            mylist[i-1]=str(int(mylist[i-1])*int(mylist[i+1]))
            mylist.pop(i)
            mylist.pop(i)
        else:
            i+=1          
    i=0
    while i<len(mylist):
        if mylist[i]=='+':
            if i==0 or mylist[i-1]=='(' :
                mylist.pop(i)
            else:
                mylist[i-1]=str(int(mylist[i-1])+int(mylist[i+1]))
                mylist.pop(i)
                mylist.pop(i)
        elif mylist[i]=='-':
            if i==0 or mylist[i-1]=='(' :
                mylist[i+1]=str(int(mylist[i+1])*(-1))
                mylist.pop(i)
            else:
                mylist[i-1]=str(int(mylist[i-1])-int(mylist[i+1]))
                mylist.pop(i)
                mylist.pop(i)     
        else:
            i+=1
    return mylist[0]


def calculate(s):
    start=[]
    s=s.replace(" ","")
    if ('+' not in s) and ('-' not in s) and ('*' not in s) and ('(' not in s):
        return int(s)
    
    s = re.findall(r'\d+|\D', s)   
    j=0
    while j<len(s):
        if s[j]=='(':
            start.append(j)
            j+=1
        elif s[j]==')':
            found=True
            end=j
            distance=end-start[-1]
            s[start[-1]]=calculations(s[start[-1]+1:end])
            for i in range(distance):
                s.pop(start[-1]+1)
                j-=1        
            start.pop(len(start)-1)
        else:
            j+=1
    return int(calculations(s))
            
            
            
    
#s=" 2-1 *2*4 "
#s=" 2-1 + 2 "
s = "(1+(4+5+2)-3)+(6+8)"
#s="1-(-2)"
result=calculate(s)
print(result)