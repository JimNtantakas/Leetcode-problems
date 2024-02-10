def minSubArrayLen(target, nums):
    min_len=float('inf')
    current_sum=0
    count=0
    for i in range(len(nums)):
        current_sum+=nums[i]
        while (current_sum>=target):
            min_len=min(min_len,i-count+1)
            print(i,count)
            current_sum-=nums[count]
            count+=1
    return min_len if min_len!=float('inf') else 0


target = 4
nums = [1,4,4]

target = 15
nums = [1,2,3,4,5]

target = 7
nums = [2,3,1,2,4,3]

result=minSubArrayLen(target,nums)
print(result)