from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        index_list = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue  # skip duplicate first elements

            left = i + 1
            right = len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    triplet = [nums[i], nums[left], nums[right]]
                    if triplet not in index_list:
                        index_list.append(triplet)

                    # Skip duplicates for left and right
                    left += 1
                    right -= 1
                    # while left < right and nums[left] == nums[left - 1]:
                    #     left += 1
                    # while left < right and nums[right] == nums[right + 1]:
                    #     right -= 1

                elif total < 0:
                    left += 1
                else:
                    right -= 1

        return index_list

# Example usage
sol = Solution()
print(sol.threeSum([3,-2,1,0]))  # Expected: [[-1, -1, 2], [-1, 0, 1]]