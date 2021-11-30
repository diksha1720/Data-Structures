# Given the root of a binary tree, return the sum of every tree node's tilt.

# The tilt of a tree node is the absolute difference between the sum of all left subtree node values and all right subtree node values. If a node does not have a left child, then the sum of the left subtree node values is treated as 0. The rule is similar if there the node does not have a right child.

 
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def helper(root):
            if root is None:
                return 0
            
            left, right = helper(root.left), helper(root.right)
            self.res += abs(left - right)
            return root.val + left + right
        
        helper(root)
        return self.res