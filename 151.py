def reverseWords(s):
    mylist=list(s)
    #removing all starting and ending spaces
    while mylist[0]==' ':
        mylist.pop(0)
    while mylist[len(mylist)-1]==' ':
        mylist.pop(len(mylist)-1)
    #removing all the between-words spaces (if more than 1)
    i=0    
    while i<len(mylist)-2:
        if mylist[i]==mylist[i+1]==' ':
            mylist.pop(i)
        else:
            i+=1
    #reverse the words 
    mystr=""
    end=len(mylist)
    for i in range (len(mylist)-1,-1,-1):
        if  mylist[i]==' ':
            for ch in mylist[i+1:end]:
                mystr+=ch
            mystr+=" "
            end=i 
        elif i==0:
            for ch in mylist[i:end]:
                mystr+=ch
    return mystr


"""def twolineapproach(s):
        s = s.split()
        print(s)
        return " ".join(s[::-1])"""

