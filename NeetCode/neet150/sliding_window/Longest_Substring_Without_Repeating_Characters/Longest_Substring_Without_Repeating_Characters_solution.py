from typing import List
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        max_substring_count, curr_count = 1, 1
        left = 0 
        right = 1
        n = len(s)
        seen = set()

        while (right != n):
            if s[left] != s[right] and s[left] not in seen:
                curr_count += 1
                seen.add(s[right])
                max_substring_count = max(curr_count, max_substring_count)
                right += 1
            else:
                left += 1
                curr_count = right - left
        return max_substring_count

sol = Solution()
result = sol.lengthOfLongestSubstring(s="pwwkew")
print(result)