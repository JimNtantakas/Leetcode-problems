def threeSum(nums):
    mylist=[]
    nums=sorted(nums)
    for j in range(len(nums)-2):
        l=j+1
        r=len(nums)-1
        while l<r and not(nums[l]>0 and nums[r]>0 and nums[j]>0):
            if (nums[l]+nums[r]+nums[j])<0:
                l+=1
            elif (nums[l]+nums[r]+nums[j])>0:
                r-=1
            else:
                if [nums[l],nums[r],nums[j]] not in mylist:
                    mylist.append([nums[l],nums[r],nums[j]])
                l+=1
                r-=1
                
    return mylist