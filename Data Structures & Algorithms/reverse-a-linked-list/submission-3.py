# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def revRec(currHead):
            if not currHead or not currHead.next :
                return currHead,currHead
            
            newHead,newTail=revRec(currHead.next)
            newTail.next=currHead
            currHead.next=None

            return newHead,currHead

        head,tail=revRec(head)
        return head
        # # reverse a linked list
        # curr=head
        # prev=None
        # fwd=None
        # while curr:
        #     fwd=curr.next
        #     curr.next=prev
        #     prev=curr
        #     curr=fwd
        # return prev





        