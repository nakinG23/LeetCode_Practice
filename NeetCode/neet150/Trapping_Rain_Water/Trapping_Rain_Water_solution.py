from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        prefix_array = [0]
        suffix_array = []
        water_heights = [0 for _ in range(len(height))]
        if len(height) < 3:
            return 0
        else:
            for i in range(1,len(height)):
                prefix_array.append(max(height[:i]))
                suffix_array.append(max(height[i:]))
                if i == len(height)-1:
                    suffix_array.append(0)   

            print("prefix = ", prefix_array, "suffix = ", suffix_array)
            
            for i in range(len(height)):    
                curr = min(prefix_array[i], suffix_array[i]) - height[i]
                if curr < 0:
                    water_heights[i] = 0
                else:
                    water_heights[i] = curr

            print("Water Heights = ", water_heights)
            print(sum(water_heights))
            return sum(water_heights)

sol = Solution()
result = sol.trap(height=[0])
print(result)

# prefix =  [0, 0, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3] 
# suffix =  [3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 1, 0]
# Heights=  [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
# Water  =  [0, 0, 1, 0, 1, 2, 1, 0, 0, 0, 0, 0]

# prefix =        [0, 0, 2, 2, 3, 3, 3, 3, 3, 3] 
# suffix =        [3, 3, 3, 3, 3, 3, 3, 2, 1, 0]
# height =        [0, 2, 0, 3, 1, 0, 1, 3, 2, 1]
# res_should_be = [0, 0, 2, 0, 2, 3, 2, 0, 0, 0]