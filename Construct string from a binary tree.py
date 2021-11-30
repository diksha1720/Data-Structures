# Given the root of a binary tree, construct a string consisting of parenthesis and integers from a binary tree with the preorder traversal way, and return it.

# Omit all the empty parenthesis pairs that do not affect the one-to-one mapping relationship between the string and the original binary tree.



class Solution:
    def __init__(self):
        self.string=''
        
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if root:
            self.string+=str(root.val)
            flag=False
            if root.left:
                flag=True
                self.string+='('
                self.tree2str(root.left)
                self.string+=')'
            if root.right:
                if not flag:
                    self.string+='()'
                self.string+='('
                self.tree2str(root.right)
                self.string+=')'
        return self.string