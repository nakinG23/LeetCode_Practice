from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        dd_nums = list(set(sorted_nums))
        count = 1
        count_list = []
        for i in range(len(dd_nums)-1):
            if (dd_nums[i] + 1) == (dd_nums[i + 1]):
                count += 1
                if not count_list and i == len(dd_nums) - 2:
                    count_list.append(count)
            else:
                count_list.append(count)
                count = 1
        if not count_list:
            return 0
        else:        
            return((max(count_list)))

sol = Solution()
# nums = [2,20,4,10,3,4,5] 
nums = [0]
result = sol.longestConsecutive(nums)
print(result)

# this one breaks at nums = [0] :(
# need to implement a soln in O(n) time using a hash set perhaps