# Given a non-empty special binary tree consisting of nodes with the non-negative value, where each node in this tree has exactly two or zero sub-node. If the node has two sub-nodes, then this node's value is the smaller value among its two sub-nodes. More formally, the property root.val = min(root.left.val, root.right.val) always holds.

# Given such a binary tree, you need to output the second minimum value in the set made of all the nodes' value in the whole tree.

# If no such second minimum value exists, output -1 instead.





# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


import sys

class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        self.min_val=root.val
        self.res=sys.maxsize
        def helper(node):
            if node:
                helper(node.left)
                if node.val<self.min_val:
                    self.min_val=node.val
                elif node.val>self.min_val and node.val<self.res:
                    self.res=node.val
                helper(node.right)
        helper(root)
        if self.res<sys.maxsize:
            return self.res
        else:
            return -1
            
            
        