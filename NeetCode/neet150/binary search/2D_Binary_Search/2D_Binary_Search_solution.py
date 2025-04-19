from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        print(m,n)
        left, right = 0, (m*n)-1

        while left<=right:
            mid = (left+right)//2
            i = mid//n
            j = mid%n
            print(mid,i,j)
            if matrix[i][j] > target:
                right = mid - 1
            elif matrix[i][j] < target:
                left = mid + 1
            else:
                return True
        
        return False
