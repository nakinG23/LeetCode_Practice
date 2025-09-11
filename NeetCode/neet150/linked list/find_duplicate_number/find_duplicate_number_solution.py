# # solution 1:
# class Solution:
#     def findDuplicate(self, nums: List[int]) -> int:
#         nums.sort()
#         for i in range(len(nums)-1):
#             if nums[i]==nums[i+1]:
#                 return nums[i]
# Solution 2:
from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seen = set()
        for num in nums:
            if num in seen:
                return num
            seen.add(num)
        return -1
    
# array:
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seen = [0] * len(nums)
        for num in nums:
            if seen[num - 1]:
                return num
            seen[num - 1] = 1

    
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seen = set()
        for num in nums:
            if num in seen:
                return num
            seen.add(num)
        return -1
   
