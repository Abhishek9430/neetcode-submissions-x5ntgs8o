class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        q=deque()
        visited=set()
        fresh=[0]
        def induce(r,c): # rots only fresh oranges not the rotten ones and not the empty cell
            if r<0 or c<0 or r>=rows or c>=cols or (r,c) in visited or grid[r][c]!=1:
                return
            q.append((r,c))
            visited.add((r,c))
            fresh[0]-=1

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==2:
                    q.append((r,c))
                    visited.add((r,c))
                if grid[r][c]==1:
                    fresh[0]+=1

        time=0
        while q and fresh[0]>0:
            for _ in range(len(q)):
                r,c=q.popleft()
                induce(r+1,c)
                induce(r-1,c)
                induce(r,c+1)
                induce(r,c-1)
            time+=1
        if fresh[0]==0:
            return time
        else:
            return -1
        