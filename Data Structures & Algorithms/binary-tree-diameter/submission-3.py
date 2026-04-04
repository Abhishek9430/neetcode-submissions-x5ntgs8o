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

            lh,ld = diameter(root.left)
            rh,rd = diameter(root.right)
            
            hmax = 1+max(lh,rh)
            curr_dia = 1 + lh + rh
            dmax = max(curr_dia,ld,rd)
            return hmax,dmax

        dia = diameter(root)
        return dia[1]-1
        

        