# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 or not list2:
            return list1 if list1 else list2
        curr1=list1
        curr2=list2
        head=None
        if curr1.val>curr2.val:
            head=ListNode(curr2.val)
            curr2=curr2.next
        else:
            head=ListNode(curr1.val)
            curr1=curr1.next

        curr=head
        while curr1 and curr2:
            if curr1.val<curr2.val:
                curr.next=curr1
                curr1=curr1.next
            else:
                curr.next=curr2
                curr2=curr2.next
            curr=curr.next

        if curr1:
            curr.next=curr1
        elif curr2:
            curr.next=curr2

        return head

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists)==0:
            return None

        while len(lists)>1:
            merged_lists=[]
            for i in range(0,len(lists),2):
                node1=lists[i]
                node2=lists[i+1] if i+1<len(lists) else None
                merged_lists.append(self.mergeTwoLists(node1,node2))
            lists=merged_lists
        return lists[0]



        