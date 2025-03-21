from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        index_list = []
        sorted_nums = sorted(nums)
        ind_count = 0
        for i in range(len(sorted_nums)):
            target = nums[i]
            for j in range(len(sorted_nums)-1, i, -1):
                # if nums[i+1] + nums[j] == target:
                if nums[i] + nums[i+1] + nums[j] == 0:
                    index_list.append([nums[i]])
                    index_list[ind_count].append(nums[i+1])
                    index_list[ind_count].append(nums[j])
                    ind_count += 1
        return(index_list)
    
sol = Solution()
result = sol.threeSum(nums=[-1,0,1,2,-1,-4])
print(result)
