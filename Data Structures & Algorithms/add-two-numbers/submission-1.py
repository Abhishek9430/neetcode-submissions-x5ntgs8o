# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr1=l1
        curr2=l2
        carry=0
        head=None
        curr=None
        while curr1 and curr2:
            val=curr1.val+curr2.val+carry
            quo,carry=val%10,val//10
            node=ListNode(quo)
            if not head:
                head=node
                curr=head
            else:
                curr.next=node
                curr=curr.next
            curr1=curr1.next
            curr2=curr2.next

        while curr1:
            val=curr1.val+carry
            quo,carry=val%10,val//10
            node=ListNode(quo)
            curr.next=node
            curr1=curr1.next
            curr=curr.next
        
        while curr2:
            val=curr2.val+carry
            quo,carry=val%10,val//10
            node=ListNode(quo)
            curr.next=node
            curr2=curr2.next
            curr=curr.next
        
        if carry!=0:
            curr.next=ListNode(carry)
        return head


        