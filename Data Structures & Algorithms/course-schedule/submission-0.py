class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj=defaultdict(list)
        for a,b in prerequisites:
            adj[b].append(a)
        visited=set()
        path=set()
        def dfs(course):
            if course in path:
                return False
            if course in visited:
                return True 

            path.add(course)
            childs=adj[course]
            for ch in childs:
                if not dfs(ch):
                    return False
            path.remove(course)
            visited.add(course)
            return True
            
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True
        