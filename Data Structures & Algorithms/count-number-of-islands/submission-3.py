class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        if not grid:
            return 0

        seen = set()
        def bfs(r,c):
            q = deque()
            q.append((r,c))
            seen.add((r,c))
            while q:
                r,c = q.popleft()

                # expolre options

                # top row  (r-1,c)
                if 0 <=  r-1 < rows and 0 <= c < cols and (r-1,c) not in seen and grid[r-1][c] == "1":
                    seen.add((r-1,c))
                    q.append((r-1,c))
                
                # bottom (r+1,c)
                if 0 <= r+1 < rows and 0 <= c < cols and (r+1,c) not in seen and grid[r+1][c] == "1":
                    seen.add((r+1,c))
                    q.append((r+1,c))

                # left (r,c-1)
                if 0 <= r < rows and 0 <= c-1 < cols and (r,c-1) not in seen and grid[r][c-1] == "1":
                    seen.add((r,c-1))
                    q.append((r,c-1))
                
                # bottom (r,c+1)
                if 0 <= r < rows and 0 <= c+1 < cols and (r,c+1) not in seen and grid[r][c+1] == "1":
                    seen.add((r,c+1))
                    q.append((r,c+1))

        
        islands = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and (i,j) not in seen:
                    bfs(i,j)
                    islands+=1
        return islands
        