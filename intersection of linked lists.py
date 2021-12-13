# Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. If the two linked lists have no intersection at all, return null.

# For example, the following two linked lists begin to intersect at node c1:


# The test cases are generated such that there are no cycles anywhere in the entire linked structure.

# Note that the linked lists must retain their original structure after the function returns.


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        A,B=headA,headB
        while A or B:
            if A:
                A=A.next
            else:
                headB=headB.next
            if B:
                B=B.next
            else:
                headA=headA.next
        while headA is not headB:
            headA=headA.next
            headB=headB.next
        return headA