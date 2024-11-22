class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index = {}
        max_length = 0
        start = 0  # Start of the current substring
        for i, char in enumerate(s):
            if char in char_index and char_index[char] >= start:
                start = char_index[char] + 1  
            char_index[char] = i
            max_length = max(max_length, i - start + 1)

        return max_length


test1 = Solution()
s = "bbbbb"
target = test1.lengthOfLongestSubstring(s)
print (target)