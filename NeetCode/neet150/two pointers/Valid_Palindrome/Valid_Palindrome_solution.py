from typing import List
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # basically removing spaces and special characters, storing the reverse of the string in another var and then comparing them!
        cleaned_s = "".join(c for c in s if c.isalnum())
        reversed_s = "".join(reversed(cleaned_s))
        if cleaned_s.lower() == reversed_s.lower():
            return True
        else:
            return False

sol = Solution()
s = "Was it a car or a cat I saw?"
result = sol.isPalindrome(s)
print(result)