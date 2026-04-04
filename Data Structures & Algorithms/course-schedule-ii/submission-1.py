class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj=defaultdict(list)
        for a,b in prerequisites:
            adj[b].append(a)
        path=set()
        visited=set()
        res=[]
        def dfs(course):
            if course in path:
                return False
            if course in visited:
                return True

            path.add(course)
            visited.add(course)
            for child in adj[course]:
                if not dfs(child):
                    return False

            path.remove(course)
            res.append(course)
            return True


        for course in range(numCourses):
            if not dfs(course):
                return []
        return res[::-1]

        