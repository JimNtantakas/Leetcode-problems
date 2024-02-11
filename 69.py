import math

def mySqrt(x):
    if x==0 or x==1:
        return x
    left=1
    right=x-1
    
    #binary search
    while left<=right:
        mid=(right+left)//2
        #print(left,right)
        #print(mid)
        if mid*mid==x:
            return mid
        elif mid*mid>x:
            right=mid-1
        else:
            left=mid+1
    if mid*mid>x and (mid-1)*(mid-1)<x:
        return mid-1
    return mid
    
    
    
x=int(input("give number: "))
result=mySqrt(x)
print(result,math.sqrt(x)) 