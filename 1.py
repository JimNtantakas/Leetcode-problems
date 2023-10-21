
def twoSum(nums,target):
    mylist=[]
    positions=[]
    for i in range(len(nums)):
        positions.append(i)
    combined = list(zip(nums, positions))
    sorted_combined = sorted(combined, key=lambda x: x[0])
    nums,positions = zip(*sorted_combined)
    #print(nums,"  ",positions)
    l=0
    r=len(nums)-1
    while l<r:
        if (nums[l]+nums[r])<target:
            l+=1
        elif (nums[l]+nums[r])>target:
            r-=1
        else:
            mylist.append([positions[l],positions[r]])
            l+=1
            r-=1 
    return mylist




nums = [3,2,4]
target = 6
result=twoSum(nums,target)    
#result=twoSum([-3,3,2,4,9],6)        
print(result)




# BRUTE FORCE:
"""     
def twoSum(self, nums, target):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]+nums[j]==target:
                return i,j 
"""