def isPalindrome(x):
    str1=str(x)
    flag=True
    for i in range(len(str1)//2):
        if str1[i]!=str1[len(str1)-1-i]:
            flag=False
    if flag==True:
        return True