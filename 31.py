#Next_Permutation
def subarray_check(nums):
    print(nums)
    length=len(nums)-1
    if length>0:
        ptr=length-1
    else:
        return nums
    while True:
        if  ptr<0:
            #nums.sort()  # Sort the array in ascending order
            return nums 
        elif nums[ptr] < nums[length]:
            result=subarray_check(nums[ptr+1:length])
            if result==nums[ptr+1:length]:
                temp=nums[ptr]
                nums[ptr]=nums[length]
                nums[length]=temp
                sorted_part = sorted(nums[ptr+1:])
                nums[ptr+1:]=sorted_part 
                #print("nums1",nums)
                return nums    
            else:
                nums[ptr+1:length]=result
                #print("nums2",nums)
                return nums
        else:
            ptr-=1
            if ptr==-1:
                length-=1
                ptr=length-1




def nextPermutation(nums):
    length=len(nums)-1
    if length>0:
        ptr=length-1
    else:
        return nums
    while True:
        if  ptr<0:
            nums.sort()  # Sort the array in ascending order
            return nums
        elif nums[ptr] < nums[length]:
            result=subarray_check(nums[ptr+1:length])
            #print(result)
            if nums[ptr+1:length]==result:
                temp=nums[ptr]
                nums[ptr]=nums[length]
                nums[length]=temp
                sorted_part = sorted(nums[ptr+1:])
                nums[ptr+1:]=sorted_part     
            else:
                z=0
                pos=-1
                for j in range(len(nums)):
                    if j>=ptr+1 and j<length-1:
                        if nums[j]!=result[z]:
                            pos=j
                            break
                        z+=1
                nums[ptr+1:length]=result
                if pos!=-1:
                    sorted_part=sorted(nums[pos+1:])
                    nums[pos+1:]=sorted_part
            return nums
        else:
            ptr-=1
            if ptr==-1:
                length-=1
                ptr=length-1




#result=nextPermutation([1,7,8,5,7,4,1,8,5,9,7,5])  #[4,2,0,3,0,2,2]
#result=nextPermutation([1,5,9,7,5]) 
#result=nextPermutation([0,2,5,9,7,5,1]) 
result=nextPermutation([2,2,7,5,4,3,2,2,1])
print(result) 











































"""
def nextPermutation(nums):
    sorted_nums=sorted(nums)

    for i in range(len(sorted_nums)):
        mylist=[]
        for j in range(len(sorted_nums)):
            number=''
            if i<j:
                for z in range(j):  
                    if z!=i:
                        number+=str(sorted_nums[z])
                number+=str(sorted_nums[i])
                for z in range(j+1,len(sorted_nums)):
                    number+=str(sorted_nums[z])

        print(number)
        mylist.append(number)
    #cprint(mylist)





result=nextPermutation([1,2,3])
#print(result)
"""
