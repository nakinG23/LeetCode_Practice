from typing import List
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0
        for index, height in enumerate(heights):
            start = index  # this is key: we track where this height could begin
            while stack and height < stack[-1][1]:
                prev_index, prev_height = stack.pop()
                maxArea = max(maxArea, prev_height * (index - prev_index))
                start = prev_index  
            stack.append([start, height])
            print(stack)

            # [7,1,7,2,2,4]
        
        # Clear out remaining stack
        for index, height in stack:
            maxArea = max(maxArea, height * (len(heights) - index))
        
        return maxArea


        # for index, height in enumerate(heights):
        #     if not stack or height > stack[-1][1]:
        #         stack.append([index,height])
        #     elif stack and height < stack[-1][1]:
        #         print(height, stack[-1][1])
        #         while(height < stack[-1][1] and stack):
        #             area = stack[-1][1] * (index - stack[-1][0])
        #             maxArea = max(maxArea, area)
        #             stack.pop()
        #         stack.append([index,height])
        #         # print(stack)
        #     # print(maxArea)
        # return maxArea
sol = Solution()
print(sol.largestRectangleArea(heights=[7,1,7,2,2,4,6,3,8,7,9]))
    
"""
So a few initial thoughts that come to mind:
if the area we found to be the max when 
everything is combined < the highest number 
of the heights element then that element is the answer

if the bars are in increasing order, then we keep adding 
to the stack if there comes a bar smaller than the last one
then we compute the area up until the last one, store it in max
then pop until we again have an increasing or equal order? i think so
"""