# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        q=collections.deque()
        q.append(root)
        res=[]
        while q:
            qsize=len(q)
            level=[]
            for _ in range(qsize):
                root=q.popleft()
                if root:
                    level.append(root.val)
                    q.append(root.left)
                    q.append(root.right)
            if level:
                res.append(level[-1])
        return res