# Given an array of integers nums, find the maximum length of a subarray where the product of all its elements is positive.

# A subarray of an array is a consecutive sequence of zero or more values taken out of that array.

# Return the maximum length of a subarray with positive product.


class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        size = len(nums)
        pos, neg = [0 for _ in range(size)], [0 for _ in range(size)]
        if nums[0] > 0 :
            pos[0] = 1
        elif nums[0] < 0 :
            neg[0] = 1
        for idx, number in enumerate(nums[1:], 1):
            if number > 0:
                pos[idx] = pos[idx-1] + 1
                if neg[idx-1]:   
                    neg[idx] = neg[idx-1] + 1
            elif number < 0: 
                neg[idx] = pos[idx-1] + 1
                if neg[idx-1]:  
                    pos[idx] = neg[idx-1] + 1
        return max(pos)
        