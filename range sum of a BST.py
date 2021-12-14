# Given the root node of a binary search tree and two integers low and high, return the sum of values of all nodes with a value in the inclusive range [low, high].


class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        output = 0
        output = self.helper(root, output, low,high)
        return output

    def helper(self,NODE, val_sum, low, high):
        if NODE.val >= low and NODE.val <= high:
                val_sum+=NODE.val
        if NODE.left is not None and NODE.val >= low:
                val_sum=self.helper(NODE.left,val_sum,low, high)
        if NODE.right is not None and NODE.val <= high:
                val_sum=self.helper(NODE.right,val_sum,low, high)
        return val_sum
