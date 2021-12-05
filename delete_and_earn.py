# You are given an integer array nums. You want to maximize the number of points you get by performing the following operation any number of times:

# Pick any nums[i] and delete it to earn nums[i] points. Afterwards, you must delete every element equal to nums[i] - 1 and every element equal to nums[i] + 1.
# Return the maximum number of points you can earn by applying the above operation some number of times.

 


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        maxval=max(nums)
        count=[0]*(maxval+1)
        dp=[0]*(maxval+1)
        for num in nums:
            count[num]+=num
        dp[0]=count[0]
        dp[1]=count[1]
        for i in range(2,maxval+1):
            dp[i]=max((dp[i-2]+count[i],dp[i-1]))
        return dp[maxval]
    
            
        
        