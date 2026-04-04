# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isvalid(root,leftmax,rightmin):
            if not root:
                return True

            if not (leftmax<root.val<rightmin):
                return False

            leftval=isvalid(root.left,leftmax,root.val)
            rightval=isvalid(root.right,root.val,rightmin)

            return leftval and rightval
            
            

        return isvalid(root,float("-inf"),float("inf"))
        