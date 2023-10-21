def generate(numRows):
        P =[]
        P.append([1])
        if numRows==1:
            return P
        elif numRows==2:    
            P.append([1,1])
            return P
        P.append([1,1])
        lista=[]

        for i in range(2,numRows):
            lista=[]
            lista.append(1)
            for j in range(1,len(P[i-1])):
                sum=P[i-1][j-1]+P[i-1][j]
                lista.append(sum)
            lista.append(1)
            P.append(lista)

        return P