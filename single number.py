class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # visited={i:2 for i in nums}
        # for num in nums:
        #     visited[num]-=1
        # for k in visited:
        #     if visited[k]==1:
        #         return k
        # return 0
        nums.sort()
        for i in range(0,len(nums)-1,2):
            if nums[i]!=nums[i+1]:
                return nums[i]
        return nums[len(nums)-1]
            