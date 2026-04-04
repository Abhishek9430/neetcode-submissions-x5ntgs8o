# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def findlca(root,p,q):
            if not root or not p or not q:
                return root
            if root.val>p.val and root.val>q.val:
                return findlca(root.left,p,q)
            if root.val<p.val and root.val<q.val:
                return findlca(root.right,p,q)
            else:
                return root
        return findlca(root,p,q)

        