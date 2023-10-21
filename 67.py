def addBinary(a, b):
    #print(len(a)," ",len(b))
    if len(a)<len(b):
        while len(a)<len(b):
            a='0'+a
    elif len(b)<len(a):
        while len(b)<len(a):
            b='0'+b
    #print(a," ",b)
    binary=''
    carry=0
    for i in range(len(a)-1,-1,-1):
        #print(a[i]," ",b[i]," ",carry)
        if a[i]=='1' and b[i]=='1' and carry==0:
            binary+='0'
            carry=1
        elif a[i]=='1' and b[i]=='1' and carry==1:
            binary+='1'
            #carry=1
        elif a[i]=='0' and b[i]=='0' and carry==0:
            binary+='0'
        elif a[i]=='0' and b[i]=='0' and carry==1:
            binary+='1'
            carry=0
        elif ((a[i]=='0' and b[i]=='1') or (a[i]=='1' and b[i]=='0')) and carry==1:
            binary+='0'
            #carry=1
        elif ((a[i]=='0' and b[i]=='1') or (a[i]=='1' and b[i]=='0')) and carry==0:
            binary+='1'   
    if carry==1:
        binary+='1'
    binary=list(binary)
    for i in range(len(binary)//2):
        temp=binary[i]
        binary[i]=binary[len(binary)-1-i]
        binary[len(binary)-1-i]=temp 
    bitstring=''
    for x in binary:
        bitstring+=x
    return bitstring  