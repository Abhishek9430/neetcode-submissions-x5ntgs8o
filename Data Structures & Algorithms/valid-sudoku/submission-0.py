class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows,cols=len(board),len(board[0])

        rd=defaultdict(set)
        cd=defaultdict(set)
        sqd=defaultdict(set)

        # check for rows and columns and squares
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == ".":
                    continue
                if board[r][c] in rd[r]:
                    return False
                elif board[r][c] in cd[c]:
                    return False
                elif board[r][c] in sqd[(r//3,c//3)]:
                    return False

                rd[r].add(board[r][c])
                cd[c].add(board[r][c])
                sqd[(r//3,c//3)].add(board[r][c])
        return True
        