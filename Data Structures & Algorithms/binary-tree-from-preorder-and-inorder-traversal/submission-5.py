# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def findIndex(root,inorder):
            for index,value in enumerate(inorder):
                if value==root:
                    return index
            return 0
            
        def tree(preorder,inorder):
            if len(inorder)==0:
                return

            root=preorder[0]
            index=findIndex(root,inorder)
            root=TreeNode(root)

            lst=tree(preorder[1:index+1],inorder[0:index])
            rst=tree(preorder[index+1::],inorder[index+1::])

            root.left=lst
            root.right=rst

            return root
        root=tree(preorder,inorder)
        return root


        