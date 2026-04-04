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
        while curr1 and curr2:
            s=curr1.val+curr2.val+carry
            if s<10:
                val=s
                carry=0
            else:
                val=s%10
                carry=s//10

            newNode=ListNode(val)
            if not head:
                head=newNode
                currf=head
            else:
                currf.next=newNode
                currf=currf.next
            curr1=curr1.next
            curr2=curr2.next


        while curr1:
            s=curr1.val+carry
            if s<10:
                val=s
                carry=0
            else:
                val=s%10
                carry=s//10

            newNode=ListNode(val)
            if not head:
                head=newNode
                currf=head
            else:
                currf.next=newNode
                currf=currf.next
            curr1=curr1.next

        while curr2:
            s=curr2.val+carry
            if s<10:
                val=s
                carry=0
            else:
                val=s%10
                carry=s//10

            newNode=ListNode(val)
            if not head:
                head=newNode
                currf=head
            else:
                currf.next=newNode
                currf=currf.next
            curr2=curr2.next

        if carry!=0:
            currf.next=ListNode(carry)
        return head


        