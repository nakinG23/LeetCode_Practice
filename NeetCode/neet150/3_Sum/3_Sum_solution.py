from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        index_list = []
        sorted_nums = sorted(nums)
        ind_count = 0
        for i in range(len(sorted_nums)):
            for j in range(len(sorted_nums)-1, i+1, -1):
                if nums[i] + nums[i+1] + nums[j] == 0:
                    item = sorted([nums[i],nums[i+1],nums[j]])
                    print("item = ", item)
                    if item not in index_list:
                        index_list.append(item)
                    ind_count += 1
        return(index_list)
    
sol = Solution()
result = sol.threeSum(nums=[-1,0,1,2,-1,-4])
# result = sol.threeSum(nums=[3,-2,1,0])
print(result)

#  literally almost there but its okay!