# Given a non-empty array nums containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n=len(nums)
        if n==1:
            return False
        s=sum(nums)
        if s%2!=0:
            return False
        target=s//2
        memo={}
        def helper(nums,idx,target):
            if target==0:
                return True
            if target<0 or idx>=n:
                return False
            if (idx,target) not in memo:
                memo[(idx,target)]=helper(nums,idx+1,target-nums[idx]) or helper(nums,idx+1,target)
            return memo[(idx,target)]
        return helper(nums,0,target)
      