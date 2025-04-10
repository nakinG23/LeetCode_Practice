class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) < 2:
            return False
        stack = []
        for i in range(len(s)):
            if s[i] == "{":
                stack.append(s[i])
            elif s[i] == "(":
                stack.append(s[i])
            elif s[i] == "[":
                stack.append(s[i])
            elif stack and s[i] == "]" and stack[-1] == "[":
                stack.pop()
            elif stack and s[i] == ")" and stack[-1] == "(":
                stack.pop()
            elif stack and s[i] == "}" and stack[-1] == "{":
                stack.pop()
            else:
                return False
        return not stack

sol = Solution()
res = sol.isValid(s="]]")
print(res)