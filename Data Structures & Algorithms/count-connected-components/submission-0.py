class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        adj=defaultdict(list)
        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)

        visited=set()
        def dfs(node):
            visited.add(node)
            for child in adj[node]:
                if not child in visited:
                    dfs(child)
        
        count=0
        for i in range(n):
            if i not in visited:
                dfs(i)
                count+=1
        return count
    
        