class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def length(node):
            l = 0
            while node:
                l += 1
                node = node.next
            return l

        def reverse(node, k):
            if k == 1 or not node or not node.next:
                fwd = node.next
                node.next = None
                return node, node, fwd
            
            small_head, small_tail, fwd = reverse(node.next, k - 1)
            small_tail.next = node
            node.next = None
            return small_head, node, fwd

        total_len = length(head)
        num_groups = total_len // k
        curr = head
        final_head = None
        prev_tail = None

        for _ in range(num_groups):
            new_head, new_tail, next_group_start = reverse(curr, k)
            if not final_head:
                final_head = new_head
            if prev_tail:
                prev_tail.next = new_head
            prev_tail = new_tail
            curr = next_group_start

        # Connect the last group's tail to remaining nodes if any
        if prev_tail:
            prev_tail.next = curr

        return final_head
