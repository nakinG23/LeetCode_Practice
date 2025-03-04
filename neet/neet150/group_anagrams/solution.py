from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        finalstrs = []
        seen = [] 
        for i, word in enumerate(strs):
            if word in seen:
                continue

            new_group = [word]  
            seen.append(word)
 
            for j in range(i+1, len(strs)):
                if sorted(word) == sorted(strs[j]):
                    new_group.append(strs[j])
                    seen.append(strs[j])
            
            finalstrs.append(new_group)

        return finalstrs

sol = Solution()
strs = ["act","pots","tops","cat","stop","hat"]
strs = [""]
result = sol.groupAnagrams(strs)
print(result)
# Input: strs = ["act","pots","tops","cat","stop","hat"]
# Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]
