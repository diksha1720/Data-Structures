# Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

# Integers in each row are sorted from left to right.
# The first integer of each row is greater than the last integer of the previous row.

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            if row[0]<=target and row[-1]>=target:
                print("Yes")
                if row[0]==target or row[-1]==target:
                    return True
                start=0
                end=len(row)-1
                while start<end:
                    mid=((start+end)//2)+1
                    if row[mid]==target:
                        return True
                    elif row[mid]>target:
                        end=mid-1
                    elif row[mid]<target:
                        start=mid+1
        return False
        