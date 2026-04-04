# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def checkbalance(root):
            if not root:
                return 0,True

            lh,is_balanced_left=checkbalance(root.left)
            rh,is_balanced_right=checkbalance(root.right)
            h=1+max(lh,rh)
            if abs(lh-rh)<=1 and is_balanced_left and is_balanced_right:
                return h,True
            else:
                return h,False
        
        height,balance=checkbalance(root)
        return balance
        