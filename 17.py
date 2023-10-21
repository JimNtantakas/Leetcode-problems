def letterCombinations(digits):
    if len(digits)==0:
        return []  
    letters=["abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
    first_digit=int(digits[0])
    Letters=letters[first_digit-2]
    k=1
    while k<len(digits):
        mylist=[]
        dig=int(digits[k])
        lett=letters[dig-2]
        for i in range(len(Letters)):
            for j in range(len(lett)):
                mylist.append(Letters[i]+lett[j])
        k+=1
        Letters=mylist[:]
    return Letters