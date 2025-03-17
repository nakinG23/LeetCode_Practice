from typing import List
class Solution:

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for k in range(0,9,3):
            for i in range(k+3):
                row_values = [num for num in board[i] if num != '.'] # taking only numerical values
                if len(row_values) != len(set(row_values)):
                # if len(board[i]) != len(set(board[i])):
                    print("duplicates found at", board[i])
                    return False
                # else:
                seen = set()
                for row in board:
                    value = row[i]
                    if value != '.' and value in seen:
                        print("duplicates found at cokumn", board[i])
                        return False
                    seen.add(value)
                seen = set()
                # for i in range(k, k+3):
                #     for j in range(k, k+3):
                #         value = board[i][j]
                #         if value != "." and value in seen:
                #             print("duplicates found at matrix", board[i][j])
                #             return False
                #         seen.add(value)
                def get_subgrid(board, row_start, col_start):
                    return [row[col_start:col_start+3] for row in board[row_start:row_start+3]]
                
                for row in range(0, 9, 3):  # Step by 3 to get subgrid row start
                    for col in range(0, 9, 3):  # Step by 3 to get subgrid column start
                        subgrid = get_subgrid(board, row, col)
                        value = subgrid[row][col]
                        if value != "." and value in seen:
                            print("duplicates found at matrix", subgrid[row][col])
                            return False
                        seen.add(value)
        return True
sol = Solution()
board = [
    ["1",".","."],
    ["4","7","."],
    ["7",".","8"]
]

board_main = [
 ["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","8",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]
]

result = sol.isValidSudoku(board_main)
print(result)