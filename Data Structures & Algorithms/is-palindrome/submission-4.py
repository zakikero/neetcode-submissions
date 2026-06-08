class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphaNumStr = ""
        
        for c in s:
            if c.isalnum():
                alphaNumStr += c.lower()

        left = 0
        right = len(alphaNumStr) - 1
        print(alphaNumStr)
        while left < right:
            if alphaNumStr[left] != alphaNumStr[right]:
                return False
            left += 1
            right -= 1 

        return True