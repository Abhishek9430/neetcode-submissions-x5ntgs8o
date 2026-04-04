class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows=len(board)
        cols=len(board[0])
        visited=set()
        def dfs(r,c,i):
            if i==len(word):
                return True

            if (r<0 or c<0 or r>=rows or c>=cols or (r,c) in visited or word[i]!=board[r][c]):
                return False

            visited.add((r,c))

            left=dfs(r,c-1,i+1)
            right=dfs(r,c+1,i+1)
            up=dfs(r-1,c,i+1)
            down=dfs(r+1,c,i+1)
            visited.remove((r,c))
            found=(left or right or up or down)
            
            return found

        for r in range(rows):
            for c in range(cols):
                found=dfs(r,c,0)
                if found:
                    return True
        return False