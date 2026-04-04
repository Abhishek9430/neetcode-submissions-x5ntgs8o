class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        seen=set()
        def bfs(r,c):
            q=deque()
            q.append((r,c))
            seen.add((r,c))
            area=1
            while q:
                r,c=q.popleft()
                directions=[[1,0],[-1,0],[0,1],[0,-1]]
                for dr,dc in directions:
                    nr,nc=dr+r,dc+c
                    if (0<=nr<rows) and (0<=nc<cols) and (nr,nc) not in seen and grid[nr][nc]==1:
                        seen.add((nr,nc))
                        q.append((nr,nc))
                        area+=1
            return area

        
        maxArea=0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1 and (r,c) not in seen:
                    area=bfs(r,c)
                    maxArea=max(area,maxArea)
        return maxArea    