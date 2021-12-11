# An integer array is called arithmetic if it consists of at least three elements and if the difference between any two consecutive elements is the same.

# For example, [1,3,5,7,9], [7,7,7,7], and [3,-1,-5,-9] are arithmetic sequences.
# Given an integer array nums, return the number of arithmetic subarrays of nums.

# A subarray is a contiguous subsequence of the array.

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        count, len_nums = 0, len(nums)
        if len_nums > 2:
            for i in range(1, len_nums - 1):
                diff = nums[i] - nums[i - 1]
                for j in range(i + 1, len_nums):
                    if nums[j] - nums[j - 1] == diff:
                        count += 1
                    else:
                        break
        return count
            