# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def diameter(root):
            if not root:
                return 0,0

            lh,ld=diameter(root.left)
            rh,rd=diameter(root.right)

            d=1+lh+rh
            d=max(d,ld,rd)
            hmax=1+max(lh,rh)
            return hmax,d

        height,d=diameter(root)
        return d-1        