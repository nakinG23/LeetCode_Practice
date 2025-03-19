from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        num_set = set(nums)
        longest_streak = 0
        
        for num in num_set:
            if num - 1 not in num_set:  # time for a new sequence, this makes sure that only the numbers which start a sequence are pciked up
                current_streak = 1
                while num + current_streak in num_set:
                    current_streak += 1
                
                longest_streak = max(longest_streak, current_streak)
        
        return longest_streak

sol = Solution()
# nums = [2,20,4,10,3,4,5] 
nums = [0]
result = sol.longestConsecutive(nums)
print(result)
