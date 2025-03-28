from typing import List
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        
        charfreq_t = [0] * 52
        charfreq_window = [0] * 52
        n1 = len(t)
        n2 = len(s)

        for c in t:
                if c.islower():
                    charfreq_t[ord(c) - ord('a')] += 1
                else:
                    charfreq_t[ord(c) - ord('A') + 26] += 1

        for i in range(n2):
                if s[i].islower():
                    charfreq_window[ord(s[i]) - ord('a')] += 1
                else:
                    charfreq_window[ord(s[i]) - ord('A') + 26] += 1

                if s[i] in t:
                     

                if i >= n1:
                    if s[i].islower():
                        charfreq_window[ord(s[i - n1]) - ord('a')] -= 1
                    else:
                        charfreq_window[ord(s[i - n1]) - ord('A') + 26] -= 1

        print(charfreq_t)


sol = Solution()
result = sol.minWindow(s="OUZODYXAZV", t="XYZ")
print(result)