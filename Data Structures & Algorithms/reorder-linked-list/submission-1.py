# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        def breakFromMiddle(head):
            slow=head
            fast=head

            while fast.next and fast.next.next:
                slow=slow.next
                fast=fast.next.next
            
            h2=slow.next
            slow.next=None

            return head,h2

        def reverseLL(head):
            curr=head
            prev,fwd=None,None
            while curr:
                fwd=curr.next
                curr.next=prev
                prev=curr
                curr=fwd
            return prev

        h1,h2=breakFromMiddle(head)
        h2=reverseLL(h2)

        f1,c1=h1,h1
        f2,c2=h2,h2
        while c1 and c2:
            f1=f1.next
            f2=f2.next
            c1.next=c2
            c2.next=f1
            c1=f1
            c2=f2




        