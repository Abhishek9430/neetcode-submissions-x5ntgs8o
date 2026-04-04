class Solution:
    def __init__(self):
        self.currmax = float('-inf')  # Also consider initializing with -inf in case all node values are negative

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def mps(node):
            if not node:
                return 0
            
            lmax = max(mps(node.left), 0)
            rmax = max(mps(node.right), 0)

            # Use node.val instead of root.val
            self.currmax = max(self.currmax, node.val + lmax + rmax)

            # Return the max path sum with only one child allowed to propagate upward
            return node.val + max(lmax, rmax)

        mps(root)
        return self.currmax
