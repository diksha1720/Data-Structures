# Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        if len(set(nums)) == len(nums):
            return False    
        for i in range(len(nums)):
            if len(nums[i:i+k+1])!=len(set(nums[i:i+k+1])):
                return True
        return False