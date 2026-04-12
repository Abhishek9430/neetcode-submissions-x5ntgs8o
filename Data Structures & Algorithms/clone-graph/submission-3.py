"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        otn = {} # old_to_new
        def bfs(node):
            q = deque()
            q.append(node)
            copy = Node(node.val)
            otn[node] = copy
            while q:
                curr = q.popleft()
                copy = otn[curr]
                for nei in curr.neighbors:
                    if nei not in otn:
                        otn[nei] = Node(nei.val)
                        q.append(nei)
                    copy.neighbors.append(otn[nei])
            return otn[node]
        return bfs(node) if node else None

        