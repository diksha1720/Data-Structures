# Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product, and return the product.

# It is guaranteed that the answer will fit in a 32-bit integer.

# A subarray is a contiguous subsequence of the array.

 


import sys
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1:
            return nums[0]
        min_prod=[sys.maxsize-1]*n
        max_prod=[sys.maxsize]*n
        
        min_prod[0]=nums[0]
        max_prod[0]=nums[0]
        
        for  i in range(1,n):
            max_prod[i]=max(nums[i], nums[i]*min_prod[i-1],nums[i]*max_prod[i-1])
            min_prod[i]=min(nums[i], nums[i]*min_prod[i-1],nums[i]*max_prod[i-1])
        return max(max_prod)
        
        