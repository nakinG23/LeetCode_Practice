from typing import List
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        seen = list()
        n1 = len(s1)
        n2 = len(s2)
        count = 0
        for r in range(len(s2)):
            seen.append(s2[r])
            if r > n1-2:
                while count < n1:
                    if s1[count] in seen:
                        count += 1
                        print("seen = ", seen)
                    else:
                        count = 0
                        seen.pop(0)
                        break
        if count == n1:
            return True
        else:
            return False


sol = Solution()
result = sol.checkInclusion(s1="hello", s2="ooolleoooleh")
print(result)