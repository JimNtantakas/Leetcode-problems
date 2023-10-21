def kWeakestRows(mat, k):
    #print(len(mat),len(mat[0]))
    mylist=[]
    positions=[i for i in range(len(mat))]
    
    for i in range(len(mat)):
        sum=0
        for j in range(len(mat[0])):
            sum+=mat[i][j]
        mylist.append(sum)
    print(mylist)
    combined = list(zip(mylist,positions))
    sorted_combined = sorted(combined, key=lambda x: x[0])
    mat,positions = zip(*sorted_combined)
    print(mat,positions)
    mylist=[]
    for i in range(k):
        mylist.append(positions[i])
    return mylist
                    
        
        
    
    
    
"""mat=[[1,1,0,0,0],
[1,1,1,1,0],
[1,0,0,0,0],
[1,1,0,0,0],
[1,1,1,1,1]]"""
mat=[[1,1,0],[1,0,0],[1,0,0],[1,1,1],[1,1,0],[0,0,0]]
result=kWeakestRows(mat,3)
print(result)
    