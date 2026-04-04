# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def same(p,q):
            if not p and not q:
                return True

            if (not p or not q) or (p.val!=q.val):
                return False

            lsb=same(p.left,q.left)
            rsb=same(p.right,q.right)

            return lsb and rsb

        def checksub(root,sub_root):
            if not root:
                return False
            if same(root,sub_root):
                return True
            ls=checksub(root.left,sub_root)
            rs=checksub(root.right,sub_root)

            return ls or rs
        
        return checksub(root,subRoot)
            

        