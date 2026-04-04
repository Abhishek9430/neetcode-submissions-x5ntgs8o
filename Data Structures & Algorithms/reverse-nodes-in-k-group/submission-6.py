# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def length(head):
            curr=head
            length=0
            while curr:
                length+=1
                curr=curr.next
            return length


        def reverseLimit(head,limit):
            prev=None
            fwd=head
            curr=head
            while curr and limit>0:
                fwd=fwd.next
                curr.next=prev
                prev=curr
                curr=fwd
                limit-=1
            return prev,head,fwd # newhead,prevtail,nextgrpstart

        l=length(head)
        num_groups=l//k
        curr=head
        final_head=None
        prev_tail=None
        for _ in range(num_groups):
            new_head,new_tail,nxt_grp_start=reverseLimit(curr,k)
            if not final_head:
                final_head=new_head
            if prev_tail:
                prev_tail.next=new_head
            
            prev_tail=new_tail
            curr=nxt_grp_start
        
        if prev_tail:
            prev_tail.next=curr

        return final_head






