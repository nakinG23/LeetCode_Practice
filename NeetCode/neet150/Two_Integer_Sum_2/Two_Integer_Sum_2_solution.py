from typing import List
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        t_list = list()
        for i in range(n):
            for j in range(i+1,n):
                if numbers[i] + numbers[j] == target:
                    t_list.append(i+1)
                    t_list.append(j+1)
        return t_list

sol = Solution()
numbers = [1,2,3,4] 
target = 3
targ_list = sol.twoSum(numbers, target)
print(targ_list)