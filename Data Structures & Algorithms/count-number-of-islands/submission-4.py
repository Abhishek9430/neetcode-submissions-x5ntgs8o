class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        seen = set()
        def bfs(r,c):
            q = deque()
            q.append((r,c))
            while q:
                r,c = q.popleft()

                # explore up
                if 0 <= r-1 < rows and 0 <= c < cols and (r-1,c) not in seen and grid[r-1][c] == "1":
                    seen.add((r-1,c))
                    q.append((r-1,c))

                # explore down
                if 0 <= r+1 < rows and 0 <= c < cols and (r+1,c) not in seen and grid[r+1][c] == "1":
                    seen.add((r+1,c))
                    q.append((r+1,c))

                # explore left
                if 0 <= r < rows and 0 <= c-1 < cols and (r,c-1) not in seen and grid[r][c-1] == "1":
                    seen.add((r,c-1))
                    q.append((r,c-1))

                # explore right
                if 0 <= r < rows and 0 <= c+1 < cols and (r,c+1) not in seen and grid[r][c+1] == "1":
                    seen.add((r,c+1))
                    q.append((r,c+1))
        

        islands = 0
        for r in range(rows):
            for c in range(cols):
                if (r,c) not in seen and grid[r][c] == "1":
                    bfs(r,c)
                    islands+=1
        return islands
        