class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        seen=set()
        if not grid:
            return 0

        def bfs(r,c):
            q=deque()
            q.append((r,c))
            seen.add((r,c))

            while q:
                r,c=q.popleft()

                # now check all the possible neighbours
                
                # top
                if 0<=r-1<rows and 0<=c<cols and (r-1,c) not in seen and grid[r-1][c]=="1":
                    seen.add((r-1,c))
                    q.append((r-1,c))

                # bottom
                if 0<=r+1<rows and 0<=c<cols and (r+1,c) not in seen and grid[r+1][c]=="1":
                    seen.add((r+1,c))
                    q.append((r+1,c))
                
                # left
                if 0<=r<rows and 0<=c-1<cols and (r,c-1) not in seen and grid[r][c-1]=="1":
                    seen.add((r,c-1))
                    q.append((r,c-1))
                
                # right
                if 0<=r<rows and 0<=c+1<cols and (r,c+1) not in seen and grid[r][c+1]=="1":
                    seen.add((r,c+1))
                    q.append((r,c+1))



        islands=0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=="1" and (r,c) not in seen:
                    bfs(r,c) # just do bfs and iteratively all the possible positions for islands to visited so that next time they does not count
                    islands+=1
        return islands

        