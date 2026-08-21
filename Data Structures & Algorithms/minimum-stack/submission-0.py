class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []


    def push(self, val: int) -> None:
        self.stack.append(val)
        minVal = val if len(self.minStack) <= 0 else min(val, self.minStack[-1])
        self.minStack.append(minVal)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()
        
    def top(self) -> int:
        return self.stack[-1] if len(self.stack) > 0 else 0


    def getMin(self) -> int:
        return self.minStack[-1]
        
    