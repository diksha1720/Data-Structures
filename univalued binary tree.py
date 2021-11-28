# A binary tree is uni-valued if every node in the tree has the same value.

# Given the root of a binary tree, return true if the given tree is uni-valued, or false otherwise.

 
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        self.value=root.val
        self.flag=True
        def helper(node):
            if node is None:
                return True
            if node.val!=self.value:
                return False
            flag=helper(node.left) and helper(node.right)
            return flag
        return helper(root)
        
        