class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpen = {"]":"[", "}":"{", ")":"("}

        stack = []
        for c in s:
            if c == "(" or c == "{" or c == "[":
                stack.append(c)
            elif not stack or closeToOpen[c] != stack[-1]:
                return False
            else:
                stack.pop()
        return not stack