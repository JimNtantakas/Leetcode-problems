def longestPalindrome(s):
    max=maxr=maxl=0 
    S=""
    for i in range(len(s)):
        l=r=i
        while True:  #finds odd length palindromes
            if l-1>=0 and r+1<len(s):   #checks left and right from the current element
                if s[l-1]==s[r+1]:
                    if r-l+1>max:
                        max=r-l+1
                        maxr=r+1
                        maxl=l-1
                    l-=1
                    r+=1
                else:
                    break
            else:
                break

        l=r=i
        iteration=0
        while True: #finds even length palindromes
            if r+1<len(s) and iteration==0:  #checks if the right element is equal to the current
                if s[i]==s[i+1]:
                    r+=1
                    if r-l>maxr-maxl:
                        maxr=r   
                        maxl=l  
                        
            if l-1>=0 and r+1<len(s):  #checks left and right from the current element
                if s[l-1]==s[r+1]:
                    if r-l+1>max:
                        max=r-l+1
                        maxr=r+1
                        maxl=l-1
                    l-=1
                    r+=1
                else:
                    break
            else:
                break
            iteration+=1    
    for j in range(maxl,maxr+1):
        S+=s[j]

    return S
                
            



"""
### BRUTE FORCE
max=0
for i in range(len(s)):
    S=""
    for j in range(i,len(s)):
        S+=s[j]         
        flag=True
        #check if palindrome
        for z in range(len(S)//2):
            if S[z]!=S[len(S)-z-1]:
                flag=False
        if flag:
            if len(S)>max:
                max=len(S)
                longest_palindrome=S
return longest_palindrome          
"""        