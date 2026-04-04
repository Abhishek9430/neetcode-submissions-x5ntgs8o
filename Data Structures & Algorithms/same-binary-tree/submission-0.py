# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def checksame(root1,root2):
            if (not root1 and not root2):
                return True
            if (root1 and not root2) or (root2 and not root1):
                return False
            if root1.val!=root2.val:
                return False

            lsame=checksame(root1.left,root2.left)
            rsame=checksame(root1.right,root2.right)

            if lsame and rsame:
                return True
            else:
                return False

        return checksame(p,q)
    
        