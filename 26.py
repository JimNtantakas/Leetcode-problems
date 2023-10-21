def removeDuplicates(nums):
    found=[]
    for x in nums:
        if x not in found:
            found.append(x)
        
    for i in range(len(found)):
        nums[i]=found[i]
    return len(found)