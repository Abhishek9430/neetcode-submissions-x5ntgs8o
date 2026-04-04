# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q=deque()
        q.append(root)
        res = []
        while q:
            length = len(q)
            level = []
            for _ in range(length):
                child=q.popleft()
                if child:
                    q.append(child.left)
                    q.append(child.right)
                    level.append(child.val)
            if level:
                res.append(level)
        return res


        