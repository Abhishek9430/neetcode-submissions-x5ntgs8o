# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def balanced(root):
            if not root:
                return 0,True

            lh,lb=balanced(root.left)
            rh,rb=balanced(root.right)

            if abs(lh-rh)>1 or not lb or not rb:
                return 1+max(lh,rh),False
            
            return 1+max(lh,rh),True

        height,balance=balanced(root)
        return balance

        