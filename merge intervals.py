class Solution:
    def merge(self, nums: List[List[int]]) -> List[List[int]]:
        if nums == []:
            return []
        res = []
        
        nums.sort()
        
        
        for i in range(len(nums)):
            
            if i == len(nums)-1:
                res.append(nums[i])
                break
            
            if nums[i][1] < nums[i+1][0]:
                res.append(nums[i])
            
            else:
                nums[i+1][1] = max(nums[i][1], nums[i+1][1])
                nums[i+1][0] = min(nums[i][0], nums[i+1][0])    
                
        return res         