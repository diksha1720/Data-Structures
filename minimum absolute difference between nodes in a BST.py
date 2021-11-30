# Given the root of a Binary Search Tree (BST), return the minimum absolute difference between the values of any two different nodes in the tree.


class Solution:
   
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.res=[]
        def helper(node):
            if node is None:
                return
            self.res.append(node.val)
            helper(node.left)
            helper(node.right)
        helper(root)
        s=9999999
        self.res.sort()
        for i in range(len(self.res)):
            s=min(s,abs(self.res[i]-self.res[i-1]))
        return s