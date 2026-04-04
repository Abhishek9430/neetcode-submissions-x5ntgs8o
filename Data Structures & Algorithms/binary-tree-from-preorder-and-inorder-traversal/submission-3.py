# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def findroot(value,inorder):
            for idx,val in enumerate(inorder):
                if val==value:
                    return idx
            return 0

        def tree(preorder,inorder):
            if not len(inorder):
                return

            rootval=preorder[0]
            idx=findroot(rootval,inorder)
            root=TreeNode(rootval)

            lst=tree(preorder[1:idx+1],inorder[0:idx])
            rst=tree(preorder[idx+1::],inorder[idx+1::])

            root.left=lst
            root.right=rst
            
            return root

        return tree(preorder,inorder)

        