# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def lcs(root,p,q):
            if not root:
                return root
            
            if root.val>max(p.val,q.val):
                return lcs(root.left,p,q)
            elif root.val<min(p.val,q.val):
                return lcs(root.right,p,q)
            else:
                return root
        
        return lcs(root,p,q)