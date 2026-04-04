# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q=deque()
        res=[]
        q.append(root)
        while q:
            level=[]
            qlen=len(q)
            for _ in range(qlen):
                root=q.popleft()
                if root:
                    q.append(root.left)
                    q.append(root.right)
                    level.append(root.val)
            if level:
                res.append(level[-1])
        return res
                    



        