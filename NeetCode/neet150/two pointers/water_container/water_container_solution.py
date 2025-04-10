from typing import List
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights)-1
        max_ar = 0
        while(left != right):
            if heights[left] < heights[right]:
                res = heights[left] * (right-left)
                left = left + 1
            else:
                res = heights[right] * (right-left)
                right = right - 1
            # print(max_ar)
            max_ar = max(max_ar,res)
        return max_ar


sol = Solution()
result = sol.maxArea(heights=[1,7,2,5,4,7,3,6])
print(result)
# Input: height = [1,7,2,5,4,7,3,6]
# Output: 36