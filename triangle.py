# Given a triangle array, return the minimum path sum from top to bottom.

# For each step, you may move to an adjacent number of the row below. More formally, if you are on index i on the current row, you may move to either index i or index i + 1 on the next row.

 

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        r=len(triangle)
        for i in range(1,r):         
            c=len(triangle[i])
            for j in range(c):
                
                if j==0:
                    triangle[i][j]+=triangle[i-1][j]
                    
                elif j==c-1:
                    triangle[i][j]+=triangle[i-1][j-1]
                    
                else:
                    triangle[i][j]+=min(triangle[i-1][j-1],triangle[i-1][j])
                    
        return min(triangle[r-1])
                    