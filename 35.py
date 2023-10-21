def searchInsert(nums, target):
    left=0
    right=len(nums)-1
    while left<=right:
        mid=(right+left)//2
        #print("mid  ",mid)
        if nums[mid]==target:
            return mid
        elif target<nums[mid]:
            right=mid-1
        elif target>nums[mid]:
            left=mid+1
    #print(left," ",right)
    if target>nums[left-1]:
        return left
    else:
        return right+1