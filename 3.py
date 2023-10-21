def lengthOfLongestSubstring(s):
    i=0
    leng=0
    max_leng=0
    list=[]
    #while s[l]==True and s[r]==True:
    for i in range(len(s)):
        leng=0
        list=[]
        l=i
        r=i
        #while s[l] not in list and s[r]==True not in list:
        while l>0:
            if s[l] not in list:
                list.append(s[l])
                leng+=1
                l-=1
            else:
                break
        while r<len(s):
            if s[r] not in list:
                list.append(s[r])
                leng+=1
                r+=1
            else:
                break
        if leng>max_leng:
            max_leng=leng
    return max_leng       