def searchRange(nums, target):
    if nums==[]:
        return [-1,-1]
    low=0
    high=len(nums)
    position=-1
    while high>=low:
        med=(low+high)//2
        if med>=len(nums):
            break
        if target<nums[med]:
            high=med-1
        elif target>nums[med]:
            low=med+1
        else:
            position=med
            break
    #print(position) 
    if position==-1:
        return [-1,-1]
    else:
        Min=Max=position
        l=position-1
        while l>=0:
            if nums[l]==target:
                Min=l
                l-=1
            else:
                break
            
        r=position+1
        while r<len(nums):
            if nums[r]==target:
                Max=r
                r+=1
            else:
                break        
        return [Min,Max]