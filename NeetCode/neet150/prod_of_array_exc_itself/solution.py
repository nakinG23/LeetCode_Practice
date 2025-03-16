from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [1] * n

        # computing the prefix product
        prefix_prod = 1
        for i in range(n):
            output[i] = prefix_prod
            prefix_prod *= nums[i]
        print("prefix prod:", output)

        # computing the suffiz product
        suffix_prod = 1
        for i in range(n-1, -1, -1):
            output[i] *= suffix_prod
            suffix_prod *= nums[i]
        print("nums list is:", nums)
        print("suffix prod:", output)
        return output
        # product = 1
        # prod_list = []
        # for num in nums:
        #     product *= num
        # for num in nums:
        #     if num == 0:
        #         prod_list.append(int(product))
        #     else:
        #         prod_list.append(int(product/num))
        # return prod_list

sol = Solution()
nums = [1,2,4,6]
result = sol.productExceptSelf(nums)
print(result)
