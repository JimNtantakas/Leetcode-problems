def findMedianSortedArrays(nums1, nums2):
        lista=[]
        len1=len(nums1)
        len2=len(nums2)
        l1=0
        l2=0
        while l1<len1 and l2<len2:
            if nums1[l1]>nums2[l2]:
                lista.append(nums2[l2])
                l2+=1
            else:
                lista.append(nums1[l1])
                l1+=1
        if (not l1<len1):
            for j in range(l2,len2):
                lista.append(nums2[j])
        elif (not l2<len2):
            for j in range(l1,len1):
                lista.append(nums1[j])
        
        length=len(lista)
        mid=length//2
        if length%2==0:
            return (lista[mid-1]+lista[mid])/2.0
        else:
            return lista[mid]