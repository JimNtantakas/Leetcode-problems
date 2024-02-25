def divide(dividend, divisor):  
    sign=1
    if dividend*divisor<0:
        sign=-1
    
    dividend=abs(dividend)
    divisor=abs(divisor)
    
    total=0
    cnt=1
    value=dividend
    while value>=divisor:
        value-=cnt*divisor
        total+=cnt
        cnt*=2
        if value<cnt*divisor:
            cnt=1
        
    if -(2**31+1)<=sign*total<=2**31-1:
        return sign*total
    else:
        return sign*(2**31-1)
    
        
