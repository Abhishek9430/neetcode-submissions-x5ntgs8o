# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        while len(lists)>1:
            merged_lists=[]
            for i in range(0,len(lists),2):
                l1=lists[i]
                l2=lists[i+1] if i+1 < len(lists) else None
                merged_lists.append(self.mergeTwoLists(l1,l2))
            lists=merged_lists
        return lists[0]

    def mergeTwoLists(self,l1,l2):
        c1=l1
        c2=l2
        dummy=ListNode(0)
        curr=dummy
        while c1 and c2:
            if c1.val<c2.val:
                curr.next=c1
                c1=c1.next
            else:
                curr.next=c2
                c2=c2.next
            curr=curr.next
        
        if c1:
            curr.next=c1
        elif c2:
            curr.next=c2

        return dummy.next




        