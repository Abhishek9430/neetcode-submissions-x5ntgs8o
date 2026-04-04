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
        def mps(node):
            if not node:
                return 0
            
            lmax=mps(node.left)
            rmax=mps(node.right)
            lmax=max(lmax,0) #to not consider negative values
            rmax=max(rmax,0)

            self.currmax=max(self.currmax,node.val+lmax+rmax) #path sum i.e. without splitting since it may be the required path

            return node.val+max(lmax,rmax) # since while going up we need to decide which way to go i.e. split
        mps(root)
        return self.currmax
        