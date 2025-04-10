from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)  # Dictionary to store grouped anagrams

        for word in strs:
            sorted_key = "".join(sorted(word))  # Sorting characters to form key
            anagram_map[sorted_key].append(word)  # Grouping anagrams together

        return list(anagram_map.values())  # Convert dictionary values to list of lists

sol = Solution()
strs = ["act","pots","tops","cat","stop","hat"]
result = sol.groupAnagrams(strs)
print(result)