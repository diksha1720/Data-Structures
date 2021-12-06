# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

# A subarray is a contiguous part of an array.



class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum=nums[0]
        cur_sum=0
        for num in nums:
            if cur_sum<0:
                cur_sum=0
            cur_sum+=num
            maxsum=max(maxsum,cur_sum)
        return maxsum
                