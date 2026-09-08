class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = [char.lower() for char in s if char.isalpha() or char.isdigit()]
        s = "".join(l)

        left, right = 0, len(s) - 1
        while left <= right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1

        return True