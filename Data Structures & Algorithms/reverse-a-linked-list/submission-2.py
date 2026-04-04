# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # reverse a linked list
        curr=head
        prev=None
        fwd=None
        while curr:
            fwd=curr.next
            curr.next=prev
            prev=curr
            curr=fwd
        return prev





        