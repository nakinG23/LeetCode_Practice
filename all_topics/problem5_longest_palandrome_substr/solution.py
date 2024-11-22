class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest_pal_substr = []
        n = len(s)
        counts = []
        count=0
        longest_substr = {}
        for i, char in enumerate(s):
            if s[i] == s[n-1-i]:
                substr = s[i:n-i]
                m = len(substr)
                print(substr, m)
                for j in range(int(m/2)):
                    if substr[j] == substr[m-1-j]:
                        print("substr[j], substr[m-1-j]")
                        print(substr[j], substr[m-1-j])
                        count = count + 1
                if count > 1:    
                    longest_substr[i] = substr
                counts.append(count)
                count = 0
        print(counts)
        print(longest_substr)
        return 2

test = Solution()
s = "dsdxabbayui"
result = test.longestPalindrome(s)
print(result)