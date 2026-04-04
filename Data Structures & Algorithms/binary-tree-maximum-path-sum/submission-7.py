# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.currmax=0
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.currmax=root.val
        def mps(root):
            if not root:
                return 0

            lmax=mps(root.left)
            rmax=mps(root.right)
            lmax=max(lmax,0)
            rmax=max(rmax,0)
            self.currmax=max(self.currmax,lmax+rmax+root.val)

            return root.val + max(lmax,rmax)

        mps(root)
        return self.currmax
        