# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

# Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

 

class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        if n==0:
            return 0
        if n==1:
            return nums[0]
        dp=[None]*(n+1)
        dp[0]=0
        dp[1]=nums[0]
        for i in range(2,n+1):
            if dp[i-1]<dp[i-2]+nums[i-1]:
                dp[i]=dp[i-2]+nums[i-1]
            else:
                dp[i]=dp[i-1]
        return dp[n]






        