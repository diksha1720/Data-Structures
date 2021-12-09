# Given an array of non-negative integers arr, you are initially positioned at start index of the array. When you are at index i, you can jump to i + arr[i] or i - arr[i], check if you can reach to any index with value 0.

# Notice that you can not jump outside of the array at any time.


class Solution:
    
    def canReach(self, arr: List[int], start: int) -> bool:
        n=len(arr)
        visited=set()
        
        def helper(start,visited):
            
            if start<0 or start>n-1:
                return False
            
            if start in visited:
                return False  
            
            if arr[start] == 0:
                return True
            
            visited.add(start)
            
            high = helper(start + arr[start],visited)
            low = helper(start - arr[start],visited)
            
            return high or low
        
        return helper(start,visited)
    




