# Given the root of a binary tree, return the preorder traversal of its nodes' values.


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result=[]
        def helper(node):
            if node is None:
                return
            result.append(node.val)
            helper(node.left)
            helper(node.right)
        helper(root)
        return result