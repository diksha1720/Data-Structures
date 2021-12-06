# Given a circular integer array nums of length n, return the maximum possible sum of a non-empty subarray of nums.

# A circular array means the end of the array connects to the beginning of the array. Formally, the next element of nums[i] is nums[(i + 1) % n] and the previous element of nums[i] is nums[(i - 1 + n) % n].

# A subarray may only include each element of the fixed buffer nums at most once. Formally, for a subarray nums[i], nums[i + 1], ..., nums[j], there does not exist i <= k1, k2 <= j with k1 % n == k2 % n.


class Solution:
    def maxSubarray(self,nums):
        maxsum=nums[0]
        cur_sum=0
        for num in nums:
            if cur_sum<0:
                cur_sum=0
            cur_sum+=num
            maxsum=max(cur_sum,maxsum)
        return maxsum
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        if all([True if num < 0 else False for num in nums]):
            return max(nums)
        else:
            arr_sum=sum(nums)
            nums_min=[]
            for num in nums:
                nums_min.append(-1*(num))
            arr_min = -self.maxSubarray(nums_min)
            arr_max=self.maxSubarray(nums)
            arr_max=max(arr_sum - arr_min, arr_max)
        return arr_max
            