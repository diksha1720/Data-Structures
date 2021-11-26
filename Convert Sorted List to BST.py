# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Given the head of a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

# For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.


class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        values=[]
        while(head):
            values.append(head.val)
            head=head.next
        def Addnode(start,end):
            if start>end:
                return None
            mid=(start+end)//2
            root=TreeNode(values[mid])
            root.left=Addnode(start,mid-1)
            root.right=Addnode(mid+1,end)
            return root
        return Addnode(0,len(values)-1)
    