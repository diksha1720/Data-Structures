# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp=head
        prev=ListNode(-101)
        # visited=[]
        while(temp):
            if temp.val==prev.val:
                prev.next=temp.next
            else:
                prev=temp
            temp=temp.next
        return head
            
        