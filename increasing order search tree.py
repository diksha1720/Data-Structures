# Given the root of a binary search tree, rearrange the tree in in-order so that the leftmost node in the tree is now the root of the tree, and every node has no left child and only one right child.

 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        self.res=[]
        A=TreeNode()
        self.temp=A
        def inOrder(node):
            if node:
                inOrder(node.left)
                self.res.append(node.val)
                inOrder(node.right)
        inOrder(root)
        A=TreeNode(self.res[0])
        temp=A
        i=1
        while i<len(self.res):
            temp.right=TreeNode(self.res[i])
            temp=temp.right
            i+=1
        return A
            