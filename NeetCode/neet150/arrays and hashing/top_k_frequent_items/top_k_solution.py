from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_dict = {} 
        for num in nums:  
            if num in count_dict:
                count_dict[num] += 1 
            else:
                count_dict[num] = 1
        print(count_dict)
        top_keys = sorted(count_dict, key=count_dict.get, reverse=True)
        print(top_keys[:k])

sol = Solution()
nums = [1,2,2,3,3,3]
k = 2
sol.topKFrequent(nums,k)
# Input: nums = [1,2,2,3,3,3], k = 2
# Output: [2,3]