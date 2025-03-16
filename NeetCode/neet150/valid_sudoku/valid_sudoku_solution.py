from typing import List
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(3):
            row_values = [num for num in board[i] if num != '.']  # Ignore empty cells
            if len(row_values) != len(set(row_values)):
            # if len(board[i]) != len(set(board[i])):
                print("duplicates found at", board[i])
                return False
            seen = set()
            for row in board:
                value = row[i]
                if value != '.' and value in seen:
                    return False
                seen.add(value)
            return True
sol = Solution()
board = [
    ["1","2","."],
    ["4","5","."],
    ["9","9","8"]
]
result = sol.isValidSudoku(board)
print(result)