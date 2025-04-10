from typing import List
class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack:
            self.min_stack.append(val)
        else:
            self.min_stack.append(min(val, self.min_stack[-1]))

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
            self.min_stack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        return None

    def getMin(self) -> int:
        if self.min_stack:
            return self.min_stack[-1]
        return None

L = []
i=0
Input = ["MinStack", "push", 1, "push", 2, "push", 0, "getMin", "pop", "top", "getMin"]
while(i<len(Input)):
    cmd = Input[i]

    if cmd == "MinStack":
        minStack = MinStack()
        i += 1

    elif cmd == "push":
        val = Input[i + 1]
        L.append(minStack.push(val))
        i += 2  

    elif cmd == "pop":
        L.append(minStack.pop())
        i += 1

    elif cmd == "top":
        L.append(minStack.top())
        i += 1

    elif cmd == "getMin":
        L.append(minStack.getMin())
        i += 1

print(L)