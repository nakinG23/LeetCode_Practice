from typing import List
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0 for _ in range(len(temperatures))]
        for i in range(len(temperatures)-1):
            for j in range(i+1, len(temperatures)):
                if temperatures[j] > temperatures[i]:
                    res[i] = j-i
                    break
        return res




'''
temps = [30,38,30,36,35,40,28]
             i  
for i keep adding to stack if temp is < ith temp
so if 38, add 30, 36, 35, 40 -> we pop
resul = [1,]
'''