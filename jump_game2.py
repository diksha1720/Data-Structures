# Given an array of non-negative integers nums, you are initially positioned at the first index of the array.

# Each element in the array represents your maximum jump length at that position.

# Your goal is to reach the last index in the minimum number of jumps.

# You can assume that you can always reach the last index.


class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        jumps = 1
        ladder = nums[0]
        steps = ladder
        itr = 0
        while steps >= 0:
            if itr == n - 1:
                return jumps
            ladder = max( itr + nums[itr], ladder )
            if steps == 0:
                steps = ladder - itr    
                jumps += 1            
            else:
                steps -= 1
                itr += 1
        