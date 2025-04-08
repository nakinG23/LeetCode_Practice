class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) < 2:
            return False
        stack = []
        for char in s:
            if char in "{[(":
                stack.append(char)
            elif stack and ((char == "]" and stack[-1] == "[") or 
                            (char == ")" and stack[-1] == "(") or 
                            (char == "}" and stack[-1] == "{")):
                stack.pop()
            else:
                return False
        return not stack