def convert(s, numRows):
        lista=[]
        i=0
        string=''
        times=True
        if numRows==1:
            return s
        while i<len(s):
            alist=[]
            if times==True:
                for j in range(numRows):
                    if i<len(s):
                        alist.append(s[i])
                        i+=1
                    else:
                        break
                cnt=numRows-1
            else:
                for j in range(numRows):
                    if i<len(s):
                        if j==cnt:
                            alist.append(s[i])
                            i+=1
                        else:
                            alist.append('')
                    else:
                        break                                
            while len(alist)<numRows:
                alist.append('')
            lista.append(alist)     
            if cnt==1:
                times=True
            else:
                times=False
                cnt-=1
        for j in range(numRows):
            for i in range(len(lista)):
                string+=lista[i][j]  
        return string 
