# Definition for a Node.
"""class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
# Given the root of an n-ary tree, return the preorder traversal of its nodes' values.

# Nary-Tree input serialization is represented in their level order traversal. Each group of children is separated by the null value (See examples)



class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        result=[]
        if root is None:
            return result
        stack=[root]
        while stack:
            node=stack.pop()
            result.append(node.val)
            stack+=node.children[::-1]
        return result
            
            
            