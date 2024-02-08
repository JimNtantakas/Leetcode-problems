def canJump(nums):    
    max_jump=0
    if (len(nums)==1):
        return True
    for i in range(len(nums)-1):
        if i>max_jump:
            return False
        
        if max_jump<i+nums[i]:
            max_jump=i+nums[i]
            
        if max_jump>=len(nums)-1:
            return True
    return False   

#recursion solution
"""if len(nums)==1:
    return True

for i in range(nums[0]):
    result=canJump(nums[i+1:])
    if result==True:  
        return True
return False    """