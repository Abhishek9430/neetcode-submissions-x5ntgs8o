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

            d=lh+rh+1 #(+1 for root from where lh and rh is calculated)
            hmax=1+max(lh,rh)
            dmax=max(d,ld,rd)
            return hmax,dmax
            
        
        hm,dm = diameter(root)
        return dm-1
        