# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def checksame(p,q):
            if not p and not q:
                return True
            if (not p and q) or (p and not q):
                return False
            if p.val!=q.val:
                return False

            leftsame=checksame(p.left,q.left)
            rightsame=checksame(p.right,q.right)

            if leftsame and rightsame:
                return True
            else:
                return False

        def checksub(root,node):
            if not root:
                return False
            if checksame(root,node):
                return True

            leftsub=checksub(root.left,node)
            rightsub=checksub(root.right,node)

            if leftsub or rightsub:
                return True
            else:
                return False

        return checksub(root,subRoot)
        