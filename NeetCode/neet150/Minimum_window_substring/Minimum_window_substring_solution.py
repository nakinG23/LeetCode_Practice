from typing import List
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        t_count, win = {}, {}
        for char in t:
            t_count[char] = 1 + t_count.get(char, 0)
        
        print("t_count: ", t_count)

        have, need = 0, len(t_count)
        print("len t_count: ", need)
        res, resLen = [-1, -1], float("infinity")
        l = 0
        for r in range(len(s)):
            c = s[r]
            win[c] = 1 + win.get(c, 0)

            if c in t_count and win[c] == t_count[c]:
                have += 1

            while have == need:
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                    
                win[s[l]] -= 1
                if s[l] in t_count and win[s[l]] < t_count[s[l]]:
                    have -= 1
                l += 1
                print(s[l : r + 1])
        l, r = res
        return s[l : r + 1] if resLen != float("infinity") else ""

sol = Solution()
result = sol.minWindow(s="OUZODYXAZV", t="XYZ")
print(result)