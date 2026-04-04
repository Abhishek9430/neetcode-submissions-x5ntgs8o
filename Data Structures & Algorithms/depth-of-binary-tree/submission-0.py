# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def depth(root):
            if not root:
                return 0
            
            l=1+depth(root.left)
            r=1+depth(root.right)
            h=max(l,r)
            return h
        
        h=depth(root)
        return h
        