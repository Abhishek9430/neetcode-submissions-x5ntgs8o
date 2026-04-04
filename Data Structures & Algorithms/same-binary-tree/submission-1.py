# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def same(p,q):
            if not p and not q:
                return True

            if (not p or not q) or (p.val!=q.val):
                return False
            
            left_equal=same(p.left,q.left)
            right_equal=same(p.right,q.right)

            if left_equal and right_equal:
                return True
            else:
                return False

        return same(p,q)

        