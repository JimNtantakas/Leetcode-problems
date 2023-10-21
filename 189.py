#Rotate_Array
def rotate(nums, k):
    while k>len(nums):
        k=k-len(nums)
    ptr=len(nums)-1
    length=ptr-k
    #print(length)
    mylist=nums[length+1:]
    #print(mylist)
    for i in range(len(nums)-k-1,-1,-1):
        #print(i+k,i)
        nums[i+k]=nums[i]

    for i in range(len(mylist)):
        nums[i]=mylist[i]
    
    return nums





#result=rotate([1,2,3,4,5,6,7],3)
#result=rotate([-1,-100,3,99],2)
result=rotate([1,2],3)
#result=rotate([1,2],5)
print(result)


"""
    for i in range(k):
        number=nums[len(nums)-1]
        for j in range(len(nums)-1,0,-1):
            nums[j]=nums[j-1]
        nums[0]=number
    return nums
"""

"""
    for i in range(k):
        mylist=[]
        number=nums.pop(len(nums)-1)
        mylist.append(number)
        mylist+=nums
        nums=[]
        nums=mylist  
    return nums
"""

"""
    ptr=len(nums)-1
    length=ptr-k
    mylist=[]
    mylist+=nums[length+1:]
    mylist+=nums[:length+1]
    nums=mylist[:]
    return nums
"""