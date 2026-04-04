class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows=len(heights)
        cols=len(heights[0])
        pac=set()
        atl=set()

        def dfs(r,c,prev_height,visited):
            if (r,c) in visited or r<0 or c<0 or r>=rows or c>=cols or heights[r][c]<prev_height:
                return
            
            visited.add((r,c))
            dfs(r+1,c,heights[r][c],visited)
            dfs(r-1,c,heights[r][c],visited)
            dfs(r,c+1,heights[r][c],visited)
            dfs(r,c-1,heights[r][c],visited)

        # top and bottom  (pac and atl)
        for c in range(cols):
            dfs(0,c,heights[0][c],pac) # pac
            dfs(rows-1,c,heights[rows-1][c],atl) #atl
        
        # left and right (pac and atl)
        for r in range(rows):
            dfs(r,0,heights[r][0],pac) #pac
            dfs(r,cols-1,heights[r][cols-1],atl) #atl

        return [[a,b] for a,b in atl.intersection(pac)]

        