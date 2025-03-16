# nums = list()
# n = input("Enter how many elements you want:")
# target = input("Enter target:")
# for i in range(int(n)):
#     num = input(f'number {i+1}: ')
#     nums.append(int(num))
# print(nums)
# print(*range(int(n)))
# for i in range(int(n)):
#     for j in range(int(i)):
#         if nums[i] + nums[j] == int(target):
#             print(f'values present at indices {i},{j} are {nums[i]},{nums[j]} and add up to target {target}')

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        final=list()
        for i in range(int(n)):
            for j in range(int(i)):
                if nums[i] + nums[j] == int(target):
                    print(f'[{i},{j}]')
                    final.append(i)
                    final.append(j)
                    return final

test_case1 = Solution.twoSum([2,7,11,15], 9)
test_case2 = Solution.twoSum([3,2,4], 6)
test_case3 = Solution.twoSum([3,3], 6)