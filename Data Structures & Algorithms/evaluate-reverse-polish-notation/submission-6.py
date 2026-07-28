class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        opStack = []
        ops = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: a / b,
        }
        result = -1
        for t in tokens:
            if t in ops:
                f, s = opStack.pop(), opStack.pop()
                result = ops[t](s,f) 
            else:
                result = t

            opStack.append(int(result))
            
        return opStack.pop()
