# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

# Merge nums1 and nums2 into a single array sorted in non-decreasing order.

# The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

class Solution:
    def merge(self,nums1: List[int], m: int, B: List[int], n: int) -> None:
        
        i=0
        j=0
        A=nums1[:m]
        temp=[]
        while(i<m and j<n):
            if A[i]<B[j]:
                temp.append(A[i])
                i+=1
            elif A[i]==B[j]:
                temp.append(A[i])
                temp.append(B[j])
                i+=1
                j+=1
            elif B[j]<A[i]:
                temp.append(B[j])
                j+=1
        if i<m:
            while(i!=m):
                temp.append(A[i])
                i+=1
        if j<n:
            while(j!=n):
                temp.append(B[j])
                j+=1
        # print(temp)
        for i in range(m+n):
            nums1[i]=temp[i]
            
           # nums1[:]=nums1[:m]
        # nums1.extend(nums2)
        # nums1.sort() 
            
        