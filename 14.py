def longestCommonPrefix(strs):
    min_length=min(len(i) for i in strs)  
    temp=''
    prefix=''
    for j in range(min_length):
        temp=strs[0][j]
        for i in range(len(strs)):
            if strs[i][j]!=temp:
                return prefix
        prefix+=temp   
    return prefix