class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1_freq = [0] * 26
        window_freq = [0] * 26

        for c in s1:
            s1_freq[ord(c) - ord('a')] += 1
        print("s1_freq = ", s1_freq)

        for i in range(len(s2)):
            window_freq[ord(s2[i])-ord('a')]+=1

            if i >= len(s1):
                window_freq[ord(s2[i-len(s1)])-ord('a')] -= 1
            
            if window_freq == s1_freq:
                return True
        
        return False

sol = Solution()
result = sol.checkInclusion(s1="hello", s2="ooolleoooleh")
print(result)