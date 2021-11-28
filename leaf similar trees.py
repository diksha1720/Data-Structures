# Consider all the leaves of a binary tree, from left to right order, the values of those leaves form a leaf value sequence.


class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        list1=self.inOrder(root1,[])
        list2=self.inOrder(root2,[])
        if list1==list2:
            return True
        return False
    
    def inOrder(self,node,temp):
        if node is None:
            return temp
        temp=self.inOrder(node.left,temp)
        if node.left is None and node.right is None:
            temp.append(node.val)
        temp=self.inOrder(node.right,temp)
        return temp
            
        