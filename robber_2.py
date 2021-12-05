# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

# Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

 


class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        if n<3:
            return max(nums)
        def helper(nums):
            n=len(nums)
            dp=[None]*(n+1)
            dp[0]=0
            dp[1]=nums[0]
            for i in range(2,n+1):
                dp[i]=max(dp[i-1],dp[i-2]+nums[i-1])
            return dp[n]
        a = helper(nums[1:])
        b = helper(nums[:-1])
        return max(a,b)
        
