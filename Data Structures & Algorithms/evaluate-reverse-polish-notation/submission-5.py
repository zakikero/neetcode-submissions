class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        opStack = []
        ops = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: a / b,
        }
        
        for t in tokens:
            if t in ops:
                f, s = opStack.pop(), opStack.pop()
                opStack.append(int(ops[t](s,f))) 
            else:
                opStack.append(int(t))
            print(opStack)

        return int(opStack[0])
