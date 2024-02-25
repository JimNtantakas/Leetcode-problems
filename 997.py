def findJudge(n, trust):
    if not len(trust)>0:
        if n==1:
            return 1
        else:
            return -1
    judge = -1    
    mylist=[]
    for i in range(n):
        mylist.append(1)
        
    for sublist in trust:
        mylist[sublist[0]-1]=0
    print(mylist)
    sum=0
    for i in range(len(mylist)):
        sum+=mylist[i]
        if mylist[i]==1:
            judge=i+1
    sum2=0
    for i in range(len(trust)):
        if trust[i][1]==judge:
            sum2+=1  
    if sum==1 and sum2==n-1:
        return judge
    return -1
    

