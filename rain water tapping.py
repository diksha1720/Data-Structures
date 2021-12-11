# 
# class Solution:Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.


    def trap(self, height: List[int]) -> int:
        if not height : return 0
        
        res = 0
        
        l_ptr , r_ptr = 0, len(height) - 1
        
        leftMax = height[l_ptr]
        rightMax = height[r_ptr]
        
        while l_ptr<r_ptr:
            if leftMax < rightMax:
                l_ptr += 1
                leftMax = max(height[l_ptr], leftMax)
                res += leftMax - height[l_ptr]
            else:
                r_ptr -= 1
                rightMax = max(height[r_ptr], rightMax)
                res += rightMax - height[r_ptr]
        return res

                
        
#  largest_so_far=height[0]
#         l_idx=0
#         for i in range(1,len(height)):
#             if height[i]>largest_so_far:
#                 l_idx=i
#                 largest_so_far=height[i]
#             if height[i]<largest_so_far:
#                 break
#         print(l_idx)
#         print(f"largest{largest_so_far}")
#         next_largest=height[l_idx+1]
#         n_idx=l_idx+1
#         for i in range(l_idx+1,len(height)):
#             if height[i]>=largest_so_far:
#                 next_largest=height[i]
#                 n_idx=i
#                 break
#             elif i==len(height)-1:
#                 return
#                 # helper(height[l_idx+1:])
#         print(f"next{next_largest}")
#         print(n_idx)
        
#         self.water+=(min(largest_so_far,next_largest)*(n_idx-l_idx-1))-sum(height[l_idx+1:n_idx])