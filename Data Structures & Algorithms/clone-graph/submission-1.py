"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        tracker={}
        def dfs(root):
            if root in tracker:
                return tracker[root]

            newRoot=Node(root.val)
            tracker[root]=newRoot

            for neis in root.neighbors:
                newRoot.neighbors.append(dfs(neis))
            
            return newRoot
        return dfs(node) if node else None
        