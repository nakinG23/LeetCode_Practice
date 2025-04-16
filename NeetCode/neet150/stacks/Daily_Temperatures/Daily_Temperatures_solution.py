from typing import List
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # res = [0 for _ in range(len(temperatures))]
        # for i in range(len(temperatures)-1):
        #     for j in range(i+1, len(temperatures)):
        #         if temperatures[j] > temperatures[i]:
        #             res[i] = j-i
        #             break
        # return res
        res = [0 for _ in range(len(temperatures))]
        stack = [] # to store temp and its index

        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]:
                indStack, tempStack = stack.pop()
                res[indStack] = (i - indStack)
            stack.append([i, temp])
        return res

sol = Solution()
print(sol.dailyTemperatures(temperatures=[30,38,30,36,35,40,28]))

'''
temps = [30,38,30,36,35,40,28]
             i  
stack = [[30,1],[38,2],[30,3],]
res   = [1,0,0,0,0,0,0]
for i keep adding to stack if temp is < ith temp
so if 38, add 30, 36, 35, 40 -> we pop
resul = [1,]
'''