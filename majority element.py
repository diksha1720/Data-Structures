# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.



class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic=Counter(nums)
        for key,value in dic.items():
            if value>len(nums)//2:
                return key
        return 0
        