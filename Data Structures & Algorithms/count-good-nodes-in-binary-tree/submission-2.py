# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def count(root,maxVal):
            if not root:
                return 0

            res = 1 if root.val>=maxVal else 0
            maxVal=max(maxVal,root.val)

            left_goodnodes = count(root.left,maxVal)
            right_goodnodes = count(root.right,maxVal)
            return res + left_goodnodes + right_goodnodes

        return count(root,root.val)
        