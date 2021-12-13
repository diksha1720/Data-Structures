# Given a binary tree, determine if it is height-balanced.

# For this problem, a height-balanced binary tree is defined as:

# a binary tree in which the left and right subtrees of every node differ in height by no more than 1.


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        if root is None:
            return True
        
        hleft=self.findMaxheight(root.left)
        hright=self.findMaxheight(root.right)
        
        if abs(hleft-hright)>1:
            return False
        
        if self.isBalanced(root.left) and self.isBalanced(root.right):
            return True
        else:
            return False
          
    def findMaxheight(self,root):
        
        if root is None:
            return 0
        
        return max(self.findMaxheight(root.left)+1,self.findMaxheight(root.right)+1)
 