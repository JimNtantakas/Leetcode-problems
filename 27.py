def removeElement(nums, val):
    cnt=0
    i=0
    while i<len(nums):
        if nums[i]==val:
            nums.remove(val)
            cnt+=1
        else:
            i+=1   
    for i in range(cnt):
        nums.append('_') 
        
    return len(nums)-cnt