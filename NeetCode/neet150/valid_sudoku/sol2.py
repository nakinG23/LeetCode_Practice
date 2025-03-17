from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows, cols, subgrids = [set() for _ in range(9)], [set() for _ in range(9)], [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                value = board[i][j]
                if value == ".":
                    continue  
                
                subgrid_index = (i // 3) * 3 + (j // 3)  #magic formula
                
                if value in rows[i] or value in cols[j] or value in subgrids[subgrid_index]:
                    return False 
                
                rows[i].add(value)
                cols[j].add(value)
                subgrids[subgrid_index].add(value)
        
        return True

sol = Solution()
board_main = [
    ["1","2",".",".","3",".",".",".","."],
    ["4",".",".","5",".",".",".",".","."],
    [".","9","1",".",".",".",".",".","3"],
    ["5",".",".",".","6",".",".",".","4"],
    [".",".",".","8",".","3",".",".","5"],
    ["7",".",".",".","2",".",".",".","6"],
    [".",".",".",".",".",".","2",".","."],
    [".",".",".","4","1","9",".",".","8"],
    [".",".",".",".","8",".",".","7","9"]
]

result = sol.isValidSudoku(board_main)
print(result)