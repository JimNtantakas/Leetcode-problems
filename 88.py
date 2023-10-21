#Merge_Sorted_Array
def merge(nums1, m, nums2, n):
    nums1[m:]=nums2
    nums1.sort()
    return nums1





nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
result=merge(nums1,m,nums2,n)
print(result)