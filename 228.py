
def summaryRanges(nums):
    ptr=0
    mylist=[]
    if len(nums)==1:
        mylist.append(str(nums[0]))
        return mylist
    for i in range(len(nums)-1):   #check if we are in the ending of the array
        if i==len(nums)-2:
            if nums[i]==nums[i+1]-1:
                mylist.append(str(nums[ptr])+"->"+str(nums[i+1]))
            else:
                if ptr!=i:
                    mylist.append(str(nums[ptr])+"->"+str(nums[i]))
                else:
                    mylist.append(str(nums[i]))
                mylist.append(str(nums[i+1]))                        
        elif nums[i]!=nums[i+1]-1:  #check if the 
            if ptr!=i:
                mylist.append(str(nums[ptr])+"->"+str(nums[i]))
                ptr=i+1
            else:
                mylist.append(str(nums[i]))
                ptr+=1
    return mylist
