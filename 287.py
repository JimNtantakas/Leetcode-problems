def findDuplicate(nums):
    sorted_nums=sorted(nums)
    low=0
    high=len(sorted_nums)
    while low<high:
        med=(low+high)//2
        if sorted_nums[med]>=(med+1):
            if sorted_nums[med]==sorted_nums[med+1]:
                return sorted_nums[med]
            low=med+1
        elif sorted_nums[med]<=(med+1):
            if sorted_nums[med]==sorted_nums[med-1]:
                return sorted_nums[med]
            high=med-1

    
#nums = [1,2,3,4,5,5,6]
#nums=[1,2,4,4,4]
nums=[1,2,3,5,6,7,8,9,9,9]
result=findDuplicate(nums)
print(result)





#WORKS ONLY IF IN NUMS THE NUMBERS ARE FROM 1 TO N (contains every number in this range)
"""
sorted_nums=sorted(nums)
low=0
high=len(sorted_nums)
while low<high:
    med=(low+high)//2
    if sorted_nums[med]==(med+1):
        if sorted_nums[med]==sorted_nums[med+1]:
            return sorted_nums[med]
        low=med+1
    elif sorted_nums[med]!=(med+1):
        if sorted_nums[med]==sorted_nums[med-1]:
            return sorted_nums[med]
        high=med-1
"""