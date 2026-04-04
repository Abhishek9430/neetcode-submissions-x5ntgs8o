# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        def breakFromMiddle(curr):
            slow=curr
            fast=curr
            while fast.next and fast.next.next:
                slow=slow.next
                fast=fast.next.next
            head1=slow
            head2=slow.next
            # break linkage
            slow.next=None
            return curr,head2

        def reverseInPlace(head2):
            curr=None
            prev=None
            while head2:
                curr=head2
                head2=head2.next
                curr.next=prev
                prev=curr
            return prev


        curr=head
        head1,head2=breakFromMiddle(head)
        # reverse second list
        revhead2=reverseInPlace(head2)
        # join the two list
        c1=head1
        c2=revhead2
        f1=c1
        f2=c2

        while f2:
            f1=c1.next
            c1.next=c2
            f2=c2.next
            c2.next=f1
            c1=f1
            c2=f2


        