# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isvalid(root,leftmin,rightmax):
            if not root:
                return True

            if not (leftmin<root.val<rightmax):
                return False

            leftval=isvalid(root.left,leftmin,root.val)
            rightval=isvalid(root.right,root.val,rightmax)

            return leftval and rightval

        return isvalid(root,float("-inf"),float("inf"))
        