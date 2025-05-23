from typing import List
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in "+-*/":
                b = stack.pop()
                a = stack.pop()
                if token == '+':
                    stack.append(a + b)
                elif token == '-':
                    stack.append(a - b)
                elif token == '*':
                    stack.append(a * b)
                else: 
                    stack.append(int(a / b))
            else:
                stack.append(int(token))
        return stack[0]


sol = Solution()
res = sol.evalRPN(tokens=["1","2","+"])
# res = sol.evalRPN(tokens=["1","2","+","3","*","4","-"])
print(res)