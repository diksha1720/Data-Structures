# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

# You must write an algorithm with O(log n) runtime complexity.


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target<min(nums):
            return 0
        if target>max(nums):
            return len(nums)
        start=0
        end=len(nums)-1
        while(start<=end):
            mid=((start+end)//2)
            if target==nums[mid]:
                return mid
            if nums[mid]<target:
                start=mid+1
            elif nums[mid]>target:
                end=mid-1
        return start
            
        