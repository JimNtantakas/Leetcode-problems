def fourSum(nums, target):
        mylist=[]
        nums=sorted(nums)
        #print(nums)
        for i in range(len(nums)-3):
            for j in range(i+1,len(nums)-2):
                l=j+1
                r=len(nums)-1
                while l<r:
                    if (nums[l]+nums[r]+nums[j]+nums[i])<target:
                        l+=1
                    elif (nums[l]+nums[r]+nums[j]+nums[i])>target:
                        r-=1
                    else:
                        if [nums[l],nums[r],nums[j],nums[i]] not in mylist:
                            mylist.append([nums[l],nums[r],nums[j],nums[i]])
                        l+=1
                        r-=1
                    
        return mylist