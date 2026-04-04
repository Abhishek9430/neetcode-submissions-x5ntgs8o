# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow=head
        fast=head
        length=0
        curr=head
        while curr:
            curr=curr.next
            length+=1
        
        index=length-n
        if index==0:
            return head.next
        curr=head
        fwd=head.next
        for _ in range(index-1):
            curr=curr.next
            fwd=fwd.next
        if fwd:
            curr.next=fwd.next
        else:
            curr.next=None
        return head


        