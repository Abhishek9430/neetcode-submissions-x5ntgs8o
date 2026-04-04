class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def checksame(p, q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            if p.val != q.val:
                return False
            return checksame(p.left, q.left) and checksame(p.right, q.right)

        def checksub(root, node):
            if not root:
                return False
            if checksame(root, node):
                return True
            return checksub(root.left, node) or checksub(root.right, node)

        return checksub(root, subRoot)
