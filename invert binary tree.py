#Given the root of a binary tree, invert the tree, and return its root.


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        A=root
        def helper(node):
            if node is None:
                return
            elif node.left and not node.right:
                temp=node.left
                node.left=None
                node.right=temp
            elif not node.left and node.right:
                temp=node.right
                node.right=None
                node.left=temp
            elif node.left and node.right:
                temp=node.left
                node.left=node.right
                node.right=temp
            helper(node.left)
            helper(node.right)
        helper(A)
        return root
            