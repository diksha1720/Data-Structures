# Given an integer numRows, return the first numRows of Pascal's triangle.

# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        final=[]       
        for i in range(1,numRows+1):
            res=[1]*i
            if i>2:
                for k in range(1,i-1):
                    res[k]=final[i-2][k-1]+final[i-2][k]
            final.append(res)     
            
        return final
        
        