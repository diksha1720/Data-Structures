
# Given the root of a Binary Search Tree and a target number k, return true if there exist two elements in the BST such that their sum is equal to the given target.


class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        def helper( root, k, seen):
            if not root:
                return None
            if (k - root.val) in seen:
                return True
            seen.add(root.val)
            left = helper(root.left, k, seen)
            right = helper(root.right, k, seen)
        
            return left or right
        return helper(root, k, set())
        
        
#         temp=self.findNode(root,[])
#         for value in temp:
#             if (k-value) in temp and temp.index(k-value)!=temp.index(value):
#                 return True
#         return False
        
#     def findNode(self,node,temp):
#         if node is None:
#             return temp
#         temp.append(node.val)
#         temp=self.findNode(node.left,temp)
#         temp=self.findNode(node.right,temp)
#         return temp