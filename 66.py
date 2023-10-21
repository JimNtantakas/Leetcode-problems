def plusOne(digits):
    length=len(digits)-1
    if digits[length]!=9:
        digits[length]+=1
        return digits
    else:
        carry=0
        for i in range(len(digits)-1,-1,-1):
            if digits[i]==9:
                digits[i]=0
                carry=1       
            else:
                if carry==1:
                    digits[i]+=1
                    carry=0
                    break
    if carry==1:
        lista=[]
        lista.append(1)
        for i in range(len(digits)):
            lista.append(digits[i])
    else:
        lista=digits[:]   
    return lista  




    #second solution (easier)
    """        number=''
    for i in range(len(digits)):
        number+=str(digits[i])
    number=int(number)
    number+=1
    number=str(number)
    lista=[]
    for num in number:
        lista.append(int(num))
    return lista"""