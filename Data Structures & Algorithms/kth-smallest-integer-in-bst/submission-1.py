# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):     
        self.res=None
        self.count=0
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.res=root.val
        self.count=k
        def ksmall(root):
            if not root:
                return

            ksmall(root.left)
            self.count-=1
            if self.count==0:
                self.res=root.val
                return
            ksmall(root.right)
        ksmall(root)
        return self.res
        