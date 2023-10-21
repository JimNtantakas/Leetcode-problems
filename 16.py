def threeSumClosest(nums,target):
    nums=sorted(nums)
    closest_num=nums[0]+nums[1]+nums[2]
    closest=abs(target-(nums[0]+nums[1]+nums[2]))
    for j in range(len(nums)-2):
        l=j+1
        r=len(nums)-1
        while l<r:
            if (nums[l]+nums[r]+nums[j])<target:
                if abs(target-(nums[l]+nums[r]+nums[j]))<closest:
                    closest=abs(target-(nums[l]+nums[r]+nums[j]))
                    closest_num=nums[l]+nums[r]+nums[j]
                l+=1
            elif (nums[l]+nums[r]+nums[j])>target:               
                if abs(target-(nums[l]+nums[r]+nums[j]))<closest:
                    closest=abs(target-(nums[l]+nums[r]+nums[j]))
                    closest_num=nums[l]+nums[r]+nums[j]
                r-=1
            else:
                return target
    return closest_num