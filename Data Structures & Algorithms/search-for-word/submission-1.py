class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row=len(board)
        col=len(board[0])
        visited=set()

        def search(r,c,i):
            if i==len(word):
                return True

            if (r<0 or c<0 or r>=row or c>=col or (r,c) in visited or board[r][c]!=word[i]):
                return False

            visited.add((r,c))
            
            #search in all four direction
            up=search(r+1,c,i+1)
            down=search(r-1,c,i+1)
            right=search(r,c+1,i+1)
            left=search(r,c-1,i+1)
            res=(up or down or left or right)
            visited.remove((r,c))
            return res
        
        for r in range(row):
            for c in range(col):
                found=search(r,c,0)
                if found:
                    return True
        return False
        