from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)<2:
            return 0
        suffix = []

        for i in range(1,len(prices)):
            suffix.append(max(prices[i:]))
            if i == len(prices)-1:
                suffix.append(0) 

        print("suffix =", suffix)

        max_profit = 0
        
        for i in range(len(prices)):
            if suffix[i] > prices[i]:
                max_profit = max(suffix[i] - prices[i], max_profit)
        return max_profit

sol = Solution()
result = sol.maxProfit(prices=[])
print("Max possible profit = ", result)