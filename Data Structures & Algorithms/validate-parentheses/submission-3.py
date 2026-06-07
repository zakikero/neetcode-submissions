class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        stack = []
        map = {"}":"{", "]":"[", ")":"("}

        for p in s:
            print(p)
            if p == ")" or p == "}" or p == "]":
                if not stack or map[p] != stack.pop():
                    return False
            else:
                stack.append(p)
        return not stack
