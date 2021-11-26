# Given the root of a binary tree, return the inorder traversal of its nodes' values.



class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result=[]
        def inorder(node):
            if node is None:
                return 
            inorder(node.left)
            result.append(node.val)
            inorder(node.right)
        inorder(root)
        return result
            