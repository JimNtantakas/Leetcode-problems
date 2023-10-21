def lengthOfLastWord(s):
    found=False
    counter=0
    i=len(s)-1

    while True:
        if found==False and s[i]!=' ':
            counter+=1
            found=True
        elif found==True and s[i]!=' ':
            counter+=1
        elif found==True and s[i]==' ':
            return counter
        if i==0:
            return counter
        i-=1