# Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

 
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if self.isMirror(root,root):
            return True
        return False
    
    def isMirror(self,root1,root2):
        if root1 is None and root2 is None:
            return True
        if root1 is not None and root2 is not None:
            if root1.val==root2.val:
                return (self.isMirror(root1.left,root2.right)) and (self.isMirror(root1.right,root2.left))      
        return False