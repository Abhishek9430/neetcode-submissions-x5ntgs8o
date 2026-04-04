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
            newRoot=Node(root.val)
            tracker[root]=newRoot
            for neighs in root.neighbors:
                if neighs not in tracker:
                    dfs(neighs)
        
        if not node:
            return None
        dfs(node)
        for root,newroot in tracker.items():
            neighbors=root.neighbors
            for neighs in neighbors:
                newroot.neighbors.append(tracker[neighs])
        return tracker[node]
        