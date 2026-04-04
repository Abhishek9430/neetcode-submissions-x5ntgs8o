# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def length(head):
            l=0
            curr=head
            while curr:
                l+=1
                curr=curr.next
            return l

        def reverse(head,pos):
            if not head or not head.next or pos==1:
                fwd=head.next
                tail=head
                return head,tail,fwd
            small_head,small_tail,fwd=reverse(head.next,pos-1)
            small_tail.next=head
            head.next=None
            return small_head,head,fwd

        l=length(head)
        num_groups=l//k
        prev_tail=None
        final_head=None
        curr=head

        for _ in range(num_groups):
            new_head,new_tail,nxt_grp_start=reverse(curr,k)
            if not final_head:
                final_head=new_head
            if prev_tail:
                prev_tail.next=new_head

            prev_tail=new_tail
            curr=nxt_grp_start

        # connect elements of last list
        if prev_tail:
            prev_tail.next=curr

        return final_head





